from django.shortcuts import render
from github import Github
import re
import requests
import os

'''def home(request):
    if request.method == 'POST':
        repo_url = request.POST.get('repo_url')
        match = re.match(r'https://github.com/([^/]+)/([^/]+)', repo_url)
        if not match:
            return render(request, 'home.html', {'error': 'Invalid GitHub URL'})
        
        username, repo_name = match.groups()
        g = Github()  # Optionally, use a token: Github('your_github_token')
        try:
            repo = g.get_repo(f"{username}/{repo_name}")
            files = repo.get_contents("")
            all_links = []

            for file in files:
                if file.type == "file" and file.path.endswith(('.md', '.txt', '.html')):  # Process text-based files
                    content = file.decoded_content.decode('utf-8', errors='ignore')
                    links = re.findall(r'(https?://[^\s]+)', content)  # Extract URLs
                    all_links.extend(links)

            return render(request, 'home.html', {'repo_url': repo_url, 'links': all_links})
        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})
    
    return render(request, 'home.html')'''


def home(request):
    if request.method == 'POST':
        repo_url = request.POST.get('repo_url')
        match = re.match(r'https://github.com/([^/]+)/([^/]+)', repo_url)
        if not match:
            return render(request, 'home.html', {'error': 'Invalid GitHub URL'})
        
        username, repo_name = match.groups()
        g = Github()  # Optionally, use a token: Github('your_github_token')
        try:
            repo = g.get_repo(f"{username}/{repo_name}")
            files = repo.get_contents("")
            all_links = []
            dead_links = []

            for file in files:
                if file.type == "file" and file.path.endswith(('.md', '.txt', '.html')):  # Process text-based files
                    content = file.decoded_content.decode('utf-8', errors='ignore')
                    links = re.findall(r'(https?://[^\s]+)', content)  # Extract URLs
                    for link in links:
                        if is_dead_link(link):
                            dead_links.append(link)
                    all_links.extend(links)

            return render(request, 'home.html', {'repo_url': repo_url, 'links': all_links, 'dead_links': dead_links})
        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})
    
    return render(request, 'home.html')


def is_dead_link(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code >= 400  # Consider 400+ status codes as dead links
    except requests.RequestException:
        return True  # Treat exceptions as dead links

def get_archive_link(url):
    archive_api = f"http://archive.org/wayback/available?url={url}"
    try:
        response = requests.get(archive_api, timeout=5).json()
        if 'archived_snapshots' in response and response['archived_snapshots']:
            return response['archived_snapshots']['closest']['url']
    except requests.RequestException:
        pass
    return None  # No archive found

# Add this cleaning function
def clean_link(link):
    return link.strip("()")
