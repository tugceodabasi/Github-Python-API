from __future__ import unicode_literals
from model.GithubAuth import GithubAuth
from service.GitHubPullsCommets import GitHubPullsCommetsServis
from service.GitHubPulls import GitHubPulls
from pick import pick
import json
from view.testInternet import interface as interface
from view.help import Help as yardim

class gereksinimler:
    if not interface.is_connected("www.google.com"):
        exit()
    yardim.yardimEkrani()
    github_username = str()
    github_password = str()
    github_username = input("GitHub Kullanıcı Adı:")
    GithubAuth.username = github_username
    github_password = input("GitHub Kullanıcı Şifresi:")
    GithubAuth.password = github_password
    github_projeAdi = str()
    github_projeKullanici = str()
    github_projeAdi = input("GitHub Proje Adi")
    GithubAuth.projeAdi = github_projeAdi
    github_projeKullanici = input("GitHub Proje Kullanıcı:")
    GithubAuth.projeKullanici = github_projeKullanici
    veriseti_dosya_yolu = str()
    veriseti_dosya_yolu = input("Veri setinin kaydedilmesi için gerekli olan dosya yolu: ")
    GithubAuth.dosyaYolu = veriseti_dosya_yolu

    print("Veri setinde olması gereken parametrelerden şu şekildedir. Veri setinde olmasını istediğiniz parametreleri seçin: ")
    parameter = ["tümü", "url", "id", "node_id", "pull_request_review_id", "diff_hunk", "path", "original_position",
                 "commit_id",
                 "original_commit_id", "in_reply_to_id", "user", "body", "created_at", "updated_at",
                 "html_url", "pull_request_url", "author_association", "start_line", "original_start_line",
                 "start_side", "line", "original_line", "side"]
    title = "Gerekli Pa1rametreleri Giriniz:"
    options = parameter
    selected = pick(options, title, multiselect=True, min_selection_count=1)
    github_parametre = []
    for i in selected:
        if (i[0] == "tümü"):
            parameter.pop(0)
            github_parametre = parameter
        else:
            github_parametre.append(i[0])
    print(github_parametre)

    jsonVeriGitHub = []
    GitHubPulls.username = GithubAuth.username
    GitHubPulls.password = GithubAuth.password
    GitHubPullsCommetsServis.username = GithubAuth.username
    GitHubPullsCommetsServis.password = GithubAuth.password
    projeKontrol = GitHubPulls.projectControl(GitHubPulls, github_projeKullanici, github_projeAdi)
    if projeKontrol == 0:
        exit()
    link = GitHubPulls.listPullLinkRequests(GitHubPulls, github_projeKullanici, github_projeAdi, pagePer=1)
    jsonNumber = []
    page = 1
    commentsArray = []
    if len(link) != 0:
        pagePer = link['last']['url'].split("=")
        jsonNumber = GitHubPulls.listPullGetNumber(GitHubPulls, github_projeKullanici, github_projeAdi, page, str(pagePer[1]))
        if len(jsonNumber) != 0:

            commentsArray = GitHubPullsCommetsServis.listCommentsOnPullRequest(GitHubPullsCommetsServis,github_projeKullanici, github_projeAdi, jsonNumber)
            if commentsArray != 0:
                with open(GithubAuth.dosyaYolu+github_projeAdi+'.json', 'w') as f:
                    json.dump(commentsArray, f)
            else:
                print("Servis Düzgün Çalışmadı")
        else:
            print("Servis Çalışamadı")
    else:
        jsonNumber = GitHubPulls.listPullGetNumber(GitHubPulls, github_projeKullanici, github_projeAdi, 1, 0)
        if len(jsonNumber) != 0:
            commentsArray = GitHubPullsCommetsServis.listCommentsOnPullRequest(GitHubPullsCommetsServis, github_projeKullanici, github_projeAdi, jsonNumber)
            if commentsArray != 0:
                with open(GithubAuth.dosyaYolu+github_projeAdi+'.json', 'w') as f:
                    json.dump(commentsArray, f)
            else:
                print("Servis Düzgün Çalışmadı")
        else:
            print("Servis Çalışamadı")

    with open(GithubAuth.dosyaYolu+github_projeAdi+'.json', 'r') as data_file:
        data = json.load(data_file)
    for element in data:
        for j in element:
            for x in github_parametre:
                if "id" not in x:
                    if 'id' in j:
                        del j['id']
                if "url" not in x:
                    if 'url' in j:
                        del j['url']
                if "node_id" not in x:
                    if 'node_id' in j:
                        del j['node_id']
                if "pull_request_review_id" not in x:
                    if 'pull_request_review_id' in j:
                        del j['pull_request_review_id']
                if "diff_hunk" not in x:
                    if 'diff_hunk' in j:
                        del j['diff_hunk']
                if "path" not in x:
                    if 'path' in j:
                        del j['path']
                if "position" not in x:
                    if 'position' in j:
                        del j['position']
                if "original_position" not in x:
                    if 'original_position' in j:
                        del j['original_position']
                if "commit_id" not in x:
                    if 'commit_id' in j:
                        del j['commit_id']
                if "original_commit_id" not in x:
                    if 'original_commit_id' in j:
                        del j['original_commit_id']
                if "in_reply_to_id" not in x:
                    if 'in_reply_to_id' in j:
                        del j['in_reply_to_id']
                if "user" not in x:
                    if 'user' in j:
                        del j['user']
                if "body" not in x:
                    if 'body' in j:
                        del j['body']
                if "created_at" not in x:
                    if 'created_at' in j:
                        del j['created_at']
                if "updated_at" not in x:
                    if 'updated_at' in j:
                        del j['updated_at']
                if "html_url" not in x:
                    if 'html_url' in j:
                        del j['html_url']
                if "pull_request_url" not in x:
                    if 'pull_request_url' in j:
                        del j['pull_request_url']
                if "author_association" not in x:
                    if 'author_association' in j:
                        del j['author_association']
                if "_links" not in x:
                    if '_links' in j:
                        del j['_links']
                if "start_line" not in x:
                    if 'start_line' in j:
                        del j['start_line']
                if "original_start_line" not in x:
                    if 'original_start_line' in j:
                        del j['original_start_line']
                if "start_side" not in x:
                    if 'start_side' in j:
                        del j['start_side']
                if "line" not in x:
                    if 'line' in j:
                        del j['line']
                if "original_line" not in x:
                    if 'original_line' in j:
                        del j['original_line']
                if "side" not in x:
                    if 'side' in j:
                        del j['side']
    with open(GithubAuth.dosyaYolu+github_projeAdi+'.json', 'w') as data_file:
        data = json.dump(data, data_file)