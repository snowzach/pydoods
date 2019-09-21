import requests
import base64


class PyDOODS:
    """A wrapper for the DOODS service"""

    def __init__(self, url, auth_key=None, timeout=90):
        self.url = url
        self.auth_key = auth_key
        self.timeout = timeout
        # Check the connection to DOODS
        self.get_detectors()

    def get_detectors(self):
        """Check the health and return the configured detectors."""
        kwargs = {"timeout": self.timeout}
        if self.auth_key:
            kwargs['headers'] = {'doods-auth-key': self.auth_key}
        response = requests.get(self.url + "/detectors", **kwargs)
        response.raise_for_status()
        return response.json()

    def detect(self, image, dconfig={}, detector_name="default", id=""):
        """Perform a detection and return the results."""
        kwargs = {"timeout": self.timeout}
        if self.auth_key:
            kwargs['headers'] = {'doods-auth-key': self.auth_key}
        response = requests.post(
            self.url + "/detect", json={"data": PyDOODS.encode_image(image), "detector_name": detector_name, "detect": dconfig, "id": id}, **kwargs)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def encode_image(image):
        """base64 encode an image stream."""
        return base64.b64encode(image).decode('ascii')
