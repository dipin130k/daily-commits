# Daily Code Sample - 2025-08-20

## Python Data Visualization Example

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create visualization
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.plot(x, y3, label='sin(x)*cos(x)', color='green')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('trig_functions.png')
```

## JavaScript Component

```javascript
class ThemeToggle {
  constructor() {
    this.theme = localStorage.getItem('theme') || 'light';
    this.initTheme();
    this.setupListeners();
  }
  
  initTheme() {
    document.body.classList.add(this.theme);
    document.documentElement.setAttribute('data-theme', this.theme);
  }
  
  setupListeners() {
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => this.toggleTheme());
    }
  }
  
  toggleTheme() {
    const newTheme = this.theme === 'light' ? 'dark' : 'light';
    document.body.classList.replace(this.theme, newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    this.theme = newTheme;
  }
}

// Initialize theme toggle
new ThemeToggle();
```
