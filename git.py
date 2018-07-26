import sys
import os
import urllib
import urllib2
import json

def get_content():
        repo_name = get_repo_name()
        committer = get_committer()
        log = get_log()
        sha_id = get_id()
        content = {'repo_name': repo_name, 'committer': committer, 'log': log, 'sha_id': sha_id}
        return content
def get_repo_name():
        return "sample.git"
def get_committer():
        cmd = 'git log --pretty=format:"%cn" -1'
        output = os.popen(cmd).read()
        return output
def get_log():
        cmd = 'git log --pretty=format:"%s" -1'
        output = os.popen(cmd).read()
        return output
def get_id():
        cmd = 'git log --pretty=format:"%h" -1'
        output = os.popen(cmd).read()
        return output
def post(content):
        url = "https://hook.worktile.com/git/abc778f664fb4035a970e9ff360d0b4c"
        data = {'payload': content}
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url = url, data = json.dumps(data), headers = headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return

os.chdir("/Volumes/Transcend/SourceTree_Clone/Learning/net_gate.git")

content = get_content()
post(content)

