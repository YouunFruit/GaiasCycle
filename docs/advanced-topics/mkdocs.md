# Welcome to Gaia Cycle Documentation

**Gaia Cycle** is a platform dedicated to sustainable urban farming and data-driven insights for a greener future. This documentation provides an overview of the project structure, setup instructions, and key features.

For more information on MkDocs, visit [mkdocs.org](https://www.mkdocs.org).

---

## Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs build --clean` - Clear caches during builds.
- `mkdocs -h` - Print help message and exit.

---

## Project Layout

```
mkdocs.yml    # Configuration file for MkDocs

docs/         # Documentation folder
    index.md  # Homepage
    images/   # Media and diagrams
    features/ # Feature documentation
    development/ # Development guides
    deployment/  # Deployment instructions
```

---

## Configuration (mkdocs.yml)

The `mkdocs.yml` file defines the site structure, theme, and additional settings:

### **Basic Configuration:**

```yaml
site_name: Gaia Cycle Documentation
repo_url: https://github.com/MarieBelle88/GaiasCycle

theme:
  name: material
  language: en
  palette:
    - scheme: default
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - scheme: slate
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  font:
    text: Roboto
    code: Roboto Mono
  features:
    - navigation.tabs
    - navigation.expand
    - content.code.copy
    - content.code.annotate
    - navigation.sections
    - navigation.instant
extra:
  generator: false

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - tables

extra_javascript:
  - https://unpkg.com/mermaid@10/dist/mermaid.min.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
```

### **Navigation:**

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Prerequisites: getting-started/prerequisites.md
      - Installation: getting-started/installation.md
      - Running the App: getting-started/running-the-app.md
  - Architecture:
      - Overview: architecture/overview.md
      - Sequence Diagrams: architecture/sequence-diagrams.md
  - Features:
      - User Pages: features/user-pages.md
      - Admin Pages: features/admin-pages.md
      - Map and Search: features/map-and-search.md
  - Development:
      - Git Workflow: development/git-workflow.md
      - Testing: development/testing.md
  - Advanced Topics:
      - Kafka: advanced-topics/kafka.md
      - API Reference: advanced-topics/api-reference.md
  - Troubleshooting: troubleshooting.md
```

---

## Additional Features

### **Dynamic Content Rendering**
- Supports **Mermaid Diagrams** for flowcharts and diagrams.
- Includes **MathJax** for rendering mathematical equations.
- Code snippets can be copied directly using the copy button.

### **Mobile-Friendly Design**
- Material theme ensures responsive layouts across devices.

### **Search and Navigation Enhancements**
- Tabbed navigation for quick access.
- Instant search for faster lookup.

---

## Final Notes

This documentation is structured to help developers and users quickly set up and navigate the Gaia Cycle platform. Follow the provided commands to build, test, and deploy the documentation site. For further assistance, contact our support team or visit the [GitHub repository](https://github.com/MarieBelle88/GaiasCycle).

