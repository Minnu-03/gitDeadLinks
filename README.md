# gitDeadLinks - Detect and Manage Broken Links in GitHub Repositories

gitDeadLinks is a Python-based tool designed to help developers identify and manage dead or broken links within GitHub repositories. It scans URLs embedded in markdown files (e.g., README.md) and checks their status to determine whether the links are functional or broken. This tool is aimed at developers who want to ensure that all links in their repositories are working, minimizing the chance of users encountering 404 errors or broken references.

<h2>Features:</h2>
<ul>
  <li><strong>Easy Scanning:</strong> Automatically scans markdown files (such as <code>README.md</code>) to extract and check all URLs for validity.</li>
  <li><strong>Broken Link Detection:</strong> Identifies and flags links that return 404 errors, lead to invalid domains, or are otherwise non-functional.</li>
  <li><strong>Fast and Efficient:</strong> Quickly checks all the links within a repository in a single pass, enabling developers to maintain clean, up-to-date documentation.</li>
</ul>

<h2>Why Use gitDeadLinks?</h2>

<ul>
  <li><strong>Keep your repository free from broken links:</strong> Regularly check and ensure all links in your repository work as expected.</li>
  <li><strong>Improve user experience:</strong> Prevent users from encountering dead links and ensure all documentation references are valid and accessible.</li>
  <li><strong>Easily find and fix dead links:</strong> With gitDeadLinks, developers can quickly spot problematic links and resolve issues, keeping their repositories tidy and reliable.</li>
</ul>

<h2>Test Links</h2>

<h3>Working Links</h3>
<ul>
  <li><a href="https://example.com" target="_blank">Example</a></li>
  <li><a href="https://github.com/Minnu-03/gitDeadLinks/blob/main/README.md" target="_blank">GitHub README</a></li>
</ul>

<h3>Example Dead Links</h3>
<ul>
  <li><a href="https://this-domain-does-not-exist-1234.com" target="_blank">Nonexistent Domain</a></li>
  <li><a href="https://example.com/this-page-does-not-exist" target="_blank">Missing Page</a></li>
</ul>

<h3>Partially Broken Link</h3>
<ul>
  <li><a href="https://httpstat.us/403" target="_blank">Forbidden Page</a></li>
</ul>

<h3>Archived Link (Optional)</h3>
<ul>
  <li><a href="https://web.archive.org/web/20220101000000/https://example.com" target="_blank">Archived Link</a></li>
</ul>
