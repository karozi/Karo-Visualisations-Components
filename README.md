
# Karo's Visualizations & Components

A curated collection of data visualization components and interactive charts designed for product managers, content creators, and data storytellers who value clean, accessible design.

## 🎯 Purpose

This repository contains reusable visualization templates and color palettes developed for the "Product with Attitude" blog. These components prioritize clarity, accessibility, and consistent branding while making complex data digestible for both technical and non-technical audiences.

## Examples

Themes Chart

👉  [Click to copy code](https://github.com/karozi/Karo-Visualisations-Components/blob/main/themes_chart.py)

👉  [View in use](https://karozieminski.substack.com/about)


<img width="2400" height="1600" alt="themes_stacked_bar" src="https://github.com/user-attachments/assets/19bb1d86-2fa3-48c5-bbf3-81bc8747d386" />

### Themes Chart
A simple stacked bar chart that tracks content themes over time. Perfect for:
- Content strategy analysis
- Editorial calendar planning
- Blog performance tracking
- Portfolio presentations

**Features:**
- ✅ Accessible color palette
- ✅ Interactive hover states
- ✅ Responsive design
- ✅ Easy monthly updates

### Design Library
A clean color swatch reference showing the standardized brand palette:
- **Forest Green** (#2B5722) - Primary for technical content
- **Charcoal Gray** (#3D3B3B) - Primary for product/UX content
- **Orange** (#FF5900) - Accent for Substack-specific content


## 🚀 Quick Start

### Prerequisites
- Modern web browser with JavaScript enabled
- Basic understanding of chart.js or similar visualization libraries

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/visualizations-components.git
   cd visualizations-components
   ```

2. **Copy the chart template:**
   ```bash
   cp themes-chart-template.html your-project/
   ```

3. **Update data values:**
   Replace the sample data with your own monthly metrics.

## 📈 Usage Examples

### Regenerating the Themes Chart

To update the chart with new monthly data:

```javascript
// Update the data object with your new values
const data = {
  months: ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"], // Add new month
  series: [
    {
      name: "AI & Tech",
      color: "#2B5722",
      data: [1,1,0,1,2,1,X] // Replace X with your count
    },
    // ... continue for other series
  ]
};
```

### Color Palette Implementation

```css
:root {
  --forest-green: #2B5722;
  --charcoal-gray: #3D3B3B;
  --accent-orange: #FF5900;
}
```

## 🎨 Design Principles

- **Accessibility First**: All visualizations meet WCAG 2.1 AA standards
- **Mobile Responsive**: Charts adapt to different screen sizes
- **Print Friendly**: Components work well in both digital and print formats
- **Consistent Branding**: Standardized color palette across all visualizations

## 📁 Repository Structure

```
├── themes-chart/
│   ├── themes-chart.html          # Main chart component
│   ├── themes-chart.js            # Chart logic and data
│   └── themes-chart.css           # Styling and responsive rules
├── design-library/
│   ├── color-palette.html         # Color swatch component
│   └── brand-guidelines.md        # Usage guidelines
├── templates/
│   └── chart-regeneration-prompt.md  # Monthly update instructions
├── assets/
│   └── preview-images/            # Component screenshots
└── docs/
    ├── accessibility-notes.md      # WCAG compliance details
    └── customization-guide.md      # How to adapt components
```

## 🔧 Customization

### Updating Colors
1. Modify the color values in the design library
2. Update CSS custom properties
3. Regenerate charts with new palette

### Adding New Chart Types
1. Follow the existing component structure
2. Maintain accessibility standards
3. Include responsive breakpoints
4. Add to the main README

## 📖 Documentation

- **[Accessibility Notes](docs/accessibility-notes.md)** - WCAG compliance details
- **[Customization Guide](docs/customization-guide.md)** - How to adapt components
- **[Chart Regeneration Prompt](templates/chart-regeneration-prompt.md)** - Monthly update template

## 🤝 Contributing

Found a bug or have a feature request? Please open an issue or submit a pull request.

### Development Guidelines
- Maintain accessibility standards
- Include responsive design considerations
- Test across modern browsers
- Update documentation for new components

## 📊 Use Cases

Perfect for:
- **Product Managers**: Tracking feature adoption, user feedback themes
- **Content Creators**: Analyzing content performance, topic distribution
- **Data Analysts**: Creating client-ready visualizations
- **Researchers**: Presenting findings with clear, accessible charts

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♀️ Author

**Karo Zieminski** - AI Product Manager  
- Blog: [Product with Attitude](https://karozieminski.substack.com/)
- Location: Helsinge, Denmark
- Focus: Building tools that actually deserve to exist

---

*These components were born from real-world needs in product management and content strategy. They're designed to be practical, accessible, and visually appealing without unnecessary complexity.*




