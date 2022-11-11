import pytest


@pytest.mark.usefixtures('init')
class TestFiles():

    header = {
        "Authorization": "admin"
    }

    def test_upload(self):
        with open('./README.md', 'r') as f:
            resp = self.bs.post(
                '/files/upload', headers=self.header, files={'file': f})
        assert resp.status_code == 200

    def test_generate_report(self):
        resp = self.bs.get('/files/generate_report/1', headers=self.header)
        assert resp.status_code == 200


    def test_get_report(self):
        resp = self.bs.get('/files/report/locust/1', headers=self.header)
        assert resp.status_code == 200
