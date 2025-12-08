# Fluid Reliability Framework - GitHub Pages Site

This directory contains the Jekyll-based GitHub Pages site for the Fluid Reliability Framework documentation.

## Local Development

### Prerequisites

- Ruby 2.7+
- Bundler (`gem install bundler`)

### Setup

```bash
cd docs
bundle install
```

### Running Locally

```bash
bundle exec jekyll serve
```

Then open `http://localhost:4000/fluid-reliability/` in your browser.

## Deploying to GitHub Pages

### Option 1: GitHub Actions (Recommended)

1. Push the `docs/` folder to your repository
2. Go to repository Settings > Pages
3. Set Source to "GitHub Actions"
4. The site will build automatically on push

### Option 2: Deploy from Branch

1. Push the `docs/` folder to your repository
2. Go to repository Settings > Pages
3. Set Source to "Deploy from a branch"
4. Select branch and `/docs` folder

## Site Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── _layouts/
│   └── default.html     # Main layout template
├── assets/
│   ├── css/
│   │   └── style.css    # Site styles
│   └── images/          # Timeline images
├── framework/
│   ├── index.md         # Framework overview
│   └── evolution.md     # Evolution through cycles
├── evidence/
│   └── index.md         # Results and validation
├── about/
│   └── index.md         # About and license
├── index.md             # Home page
├── Gemfile              # Ruby dependencies
├── LICENSE              # CC BY-NC-SA 4.0
└── README.md            # This file
```

## Configuration

Edit `_config.yml` to customize:

- `title`: Site title
- `description`: Site description
- `baseurl`: Subpath (e.g., `/fluid-reliability`)
- `url`: Base hostname
- `author`: Author information

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Author

Andrea Valenti
