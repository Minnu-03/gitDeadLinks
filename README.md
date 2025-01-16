# gitDeadLinks - Detect and Manage Broken Links in GitHub Repositories

gitDeadLinks is a Python-based tool designed to help developers identify and manage dead or broken links within GitHub repositories. It scans URLs embedded in markdown files (e.g., README.md) and checks their status to determine whether the links are functional or broken. This tool is aimed at developers who want to ensure that all links in their repositories are working, minimizing the chance of users encountering 404 errors or broken references.

<hr>

<h2>Features:</h2>

<ul>
  <li><strong>Easy Scanning:</strong> Automatically scans markdown files (such as <code>README.md</code>) to extract and check all URLs for validity.</li>
  <li><strong>Broken Link Detection:</strong> Identifies and flags links that return 404 errors, lead to invalid domains, or are otherwise non-functional.</li>
  <li><strong>Fast and Efficient:</strong> Quickly checks all the links within a repository in a single pass, enabling developers to maintain clean, up-to-date documentation.</li>
</ul>

<hr>

## Test Links

### Working Links
- [Example](https://example.com)
- https://github.com/Minnu-03/gitDeadLinks/blob/main/README.md


### Example Dead Links
- [Nonexistent Domain](https://this-domain-does-not-exist-1234.com)
- [Missing Page](https://example.com/this-page-does-not-exist)

### Partially Broken Link
- [Forbidden Page](https://httpstat.us/403)

### Archived Link (Optional)
- [Archived Link](https://web.archive.org/web/20220101000000/https://example.com)
