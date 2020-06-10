class GithubAuth:
    username = str()
    password = str()
    url = 'https://api.github.com'
    dosyaYolu = str()
    projeAdi = str()
    projeKullanici = str()
    def getUserName(self):
        return self.username
    def getPassword(self):
        return self.password
    def getUrl(self):
        return self.url
    def getDosyaYolu(self):
        return self.dosyaYolu
    def getProjeAdi(self):
        return self.projeAdi
    def getProjeKullanici(self):
        return self.projeKullanici

    def __init__(self):
        return self

