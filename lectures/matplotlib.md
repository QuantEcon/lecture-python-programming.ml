---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
translation:
  title: Matplotlib
  headings:
    Overview: Overview
    Overview::Matplotlib's Split Personality: Matplotlib's Split Personality
    The APIs: The APIs
    The APIs::The MATLAB-style API: The MATLAB-style API
    The APIs::The Object-Oriented API: The Object-Oriented API
    The APIs::Tweaks: Tweaks
    More Features: More Features
    More Features::Multiple Plots on One Axis: Multiple Plots on One Axis
    More Features::Multiple Subplots: Multiple Subplots
    More Features::3D Plots: 3D Plots
    More Features::A Customizing Function: A Customizing Function
    More Features::Style Sheets: Style Sheets
    Further Reading: Further Reading
    Exercises: Exercises
---

(matplotlib)=
```{raw} jupyter
<div id="qe-notebook-header" align="right" style="text-align:right;">
        <a href="https://quantecon.org/" title="quantecon.org">
                <img style="width:250px;display:inline;" width="250px" src="https://assets.quantecon.org/img/qe-menubar-logo.svg" alt="QuantEcon">
        </a>
</div>
```

# {index}`Matplotlib <single: Matplotlib>`

```{index} single: Python; Matplotlib
```

## Overview

ഈ lectures-ൽ ഇതിനകം [Matplotlib](https://matplotlib.org/) ഉപയോഗിച്ച് ധാരാളം figures നമ്മൾ ഉണ്ടാക്കിക്കഴിഞ്ഞു.

Matplotlib scientific computing-നായി design ചെയ്ത ഒരു മികച്ച graphics library ആണ്, അതിൽ ഉള്ളവ:

* high-quality 2D, 3D plots
* സാധാരണ formats-ലെല്ലാം (PDF, PNG, മുതലായവ) output
* LaTeX integration
* presentation-ന്റെ എല്ലാ വശങ്ങളിലും fine-grained control
* animation, മുതലായവ

### Matplotlib's Split Personality

Matplotlib വ്യത്യസ്തമായത് അതു plotting-ന് രണ്ട് വ്യത്യസ്ത interfaces നൽകുന്നു എന്നതിലാണ്.

ഒന്ന് ലളിതമായ MATLAB-style API (Application Programming Interface) ആണ്, MATLAB-ൽ നിന്ന് വരുന്നവർക്ക് പെട്ടെന്ന് ഒരു ഇടം കണ്ടെത്താൻ സഹായിക്കാൻ എഴുതിയത്.

മറ്റേത് കൂടുതൽ "Pythonic" object-oriented API ആണ്.

താഴെ വിവരിക്കുന്ന കാരണങ്ങളാൽ, രണ്ടാമത്തെ API ഉപയോഗിക്കാൻ ഞങ്ങൾ recommend ചെയ്യുന്നു.

എന്നാൽ ആദ്യം, വ്യത്യാസം എന്താണെന്ന് നോക്കാം.

## The APIs

```{index} single: Matplotlib; Simple API
```

### The MATLAB-style API

introductory treatments-ൽ കാണാവുന്ന തരത്തിലുള്ള ഒരു ലളിതമായ example ഇതാ

```{code-cell} ipython
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, 'b-', linewidth=2)
plt.show()
```

ഇത് ലളിതവും സൗകര്യപ്രദവുമാണ്, പക്ഷേ ഒരു പരിധിവരെ limited-ഉം un-Pythonic-ഉം ആണ്.

ഉദാഹരണത്തിന്, function calls-ൽ, പ്രോഗ്രാമർക്ക് അറിയാതെ തന്നെ ധാരാളം objects create ചെയ്യപ്പെടുകയും pass ചെയ്യപ്പെടുകയും ചെയ്യുന്നു.

Python programmers സാധാരണയായി കൂടുതൽ explicit ആയ ഒരു programming style ഇഷ്ടപ്പെടുന്നു (ഒരു code block-ൽ `import this` run ചെയ്ത് രണ്ടാമത്തെ line നോക്കുക).

ഇത് നമ്മെ alternative ആയ, object-oriented Matplotlib API-ലേക്ക് നയിക്കുന്നു.

### The Object-Oriented API

മുൻപത്തെ figure-ന് corresponding ആയ code object-oriented API ഉപയോഗിച്ച് ഇതാ

```{code-cell} python3
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)
plt.show()
```

ഇവിടെ `fig, ax = plt.subplots()` എന്ന call ഒരു pair return ചെയ്യുന്നു, അതിൽ

* `fig` ഒരു `Figure` instance ആണ്---ഒരു blank canvas പോലെ.
* `ax` ഒരു `AxesSubplot` instance ആണ്---plotting ചെയ്യാനുള്ള ഒരു frame ആയി കരുതുക.

`plot()` function യഥാർത്ഥത്തിൽ `ax`-ന്റെ ഒരു method ആണ്.

കുറച്ചു കൂടുതൽ typing ഉണ്ടെങ്കിലും, objects-ന്റെ ഈ explicit ആയ ഉപയോഗം നമുക്ക് മെച്ചപ്പെട്ട control നൽകുന്നു.

നമ്മൾ മുന്നോട്ട് പോകുമ്പോൾ ഇത് കൂടുതൽ വ്യക്തമാകും.

### Tweaks

ഇവിടെ ഞങ്ങൾ line-ന് red color നൽകുകയും legend ചേർക്കുകയും ചെയ്തിരിക്കുന്നു

```{code-cell} python3
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)
ax.legend()
plt.show()
```

line-നെ അല്പം transparent ആക്കാൻ `alpha`-യും ഞങ്ങൾ ഉപയോഗിച്ചു---ഇത് അതിനെ കൂടുതൽ smooth ആയി കാണിക്കുന്നു.

`ax.legend()`-നെ `ax.legend(loc='upper center')` ഉപയോഗിച്ച് മാറ്റി legend-ന്റെ location മാറ്റാവുന്നതാണ്.

```{code-cell} python3
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)
ax.legend(loc='upper center')
plt.show()
```

എല്ലാം ശരിയായി configure ചെയ്തിട്ടുണ്ടെങ്കിൽ, LaTeX ചേർക്കുന്നത് നിസ്സാരമാണ്

```{code-cell} python3
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label=r'$y=\sin(x)$', alpha=0.6)
ax.legend(loc='upper center')
plt.show()
```

ticks control ചെയ്യുന്നതും titles ചേർക്കുന്നതും മറ്റും ലളിതമാണ്

```{code-cell} python3
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label=r'$y=\sin(x)$', alpha=0.6)
ax.legend(loc='upper center')
ax.set_yticks([-1, 0, 1])
ax.set_title('Test plot')
plt.show()
```

## More Features

Matplotlib-ന് functions-ന്റെയും features-ന്റെയും ഒരു വലിയ array ഉണ്ട്, ആവശ്യം വരുമ്പോൾ കാലക്രമേണ അവ കണ്ടെത്താം.

ചിലത് മാത്രം ഞങ്ങൾ ഇവിടെ പരാമർശിക്കുന്നു.

### Multiple Plots on One Axis

```{index} single: Matplotlib; Multiple Plots on One Axis
```

ഒരേ axes-ൽ multiple plots ഉണ്ടാക്കുന്നത് ലളിതമാണ്.

randomly മൂന്ന് normal densities generate ചെയ്ത് അവയുടെ mean-ഉള്ള ഒരു label ചേർക്കുന്ന ഒരു example ഇതാ

```{code-cell} python3
from scipy.stats import norm
from random import uniform

fig, ax = plt.subplots()
x = np.linspace(-4, 4, 150)
for i in range(3):
    m, s = uniform(-1, 1), uniform(1, 2)
    y = norm.pdf(x, loc=m, scale=s)
    current_label = rf'$\mu = {m:.2}$'
    ax.plot(x, y, linewidth=2, alpha=0.6, label=current_label)
ax.legend()
plt.show()
```

### Multiple Subplots

```{index} single: Matplotlib; Subplots
```

ചിലപ്പോൾ നമുക്ക് ഒരു figure-ൽ multiple subplots വേണ്ടിവരും.

6 histograms generate ചെയ്യുന്ന ഒരു example ഇതാ

```{code-cell} python3
num_rows, num_cols = 3, 2
fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 12))
for i in range(num_rows):
    for j in range(num_cols):
        m, s = uniform(-1, 1), uniform(1, 2)
        x = norm.rvs(loc=m, scale=s, size=100)
        axes[i, j].hist(x, alpha=0.6, bins=20)
        t = rf'$\mu = {m:.2}, \quad \sigma = {s:.2}$'
        axes[i, j].set(title=t, xticks=[-4, 0, 4], yticks=[])
plt.show()
```

### 3D Plots

```{index} single: Matplotlib; 3D Plots
```

Matplotlib 3D plots നന്നായി ചെയ്യുന്നു --- ഇതാ ഒരു example

```{code-cell} python3
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm


def f(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2)

xgrid = np.linspace(-3, 3, 50)
ygrid = xgrid
x, y = np.meshgrid(xgrid, ygrid)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,
                y,
                f(x, y),
                rstride=2, cstride=2,
                cmap=cm.jet,
                alpha=0.7,
                linewidth=0.25)
ax.set_zlim(-0.5, 1.0)
plt.show()
```

### A Customizing Function

നിങ്ങൾ പതിവായി ഉപയോഗിക്കുന്ന customizations-ന്റെ ഒരു set നിങ്ങൾ കണ്ടെത്തിയേക്കാം.

നമ്മുടെ axes origin-ലൂടെ പോകണമെന്നും, ഒരു grid ഉണ്ടാകണമെന്നും നമ്മൾ സാധാരണയായി ഇഷ്ടപ്പെടുന്നു എന്ന് കരുതുക.

ഈ changes implement ചെയ്യുന്ന ഒരു custom `subplots` function build ചെയ്യാൻ object-oriented API എങ്ങനെ ഉപയോഗിക്കാം എന്നതിന്റെ [Matthew Doty](https://github.com/xcthulhu)-യുടെ ഒരു നല്ല example ഇതാ.

code ശ്രദ്ധയോടെ വായിച്ച്, എന്താണ് നടക്കുന്നതെന്ന് follow ചെയ്യാൻ കഴിയുമോ എന്ന് നോക്കുക

```{code-cell} python3
def subplots():
    "Custom subplots with axes through the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    ax.grid()
    return fig, ax


fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-2, 10, 200)
y = np.sin(x)
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)
ax.legend(loc='lower right')
plt.show()
```

custom `subplots` function

1. `fig, ax` pair generate ചെയ്യാൻ internal ആയി standard `plt.subplots` function call ചെയ്യുന്നു,
1. `ax`-ന് ആവശ്യമായ customizations വരുത്തുന്നു, ഒപ്പം
1. `fig, ax` pair-നെ calling code-ലേക്ക് പാസ് ചെയ്യുന്നു.

### Style Sheets

Matplotlib-ലെ മറ്റൊരു ഉപകാരപ്രദമായ feature [style sheets](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html) ആണ്.

uniform ആയ styles-ഉള്ള plots create ചെയ്യാൻ നമുക്ക് style sheets ഉപയോഗിക്കാം.

`plt.style.available` എന്ന attribute print ചെയ്ത് available styles-ന്റെ ഒരു list നമുക്ക് കണ്ടെത്താം


```{code-cell} python3
print(plt.style.available)
```

ഇപ്പോൾ style sheet set ചെയ്യാൻ `plt.style.use()` method നമുക്ക് ഉപയോഗിക്കാം.

ഒരു style sheet-ന്റെ പേര് എടുത്ത് ആ style ഉപയോഗിച്ച് വ്യത്യസ്തമായ plots വരയ്ക്കുന്ന ഒരു function എഴുതാം

```{code-cell} python3

def draw_graphs(style='default'):

    # Setting a style sheet
    plt.style.use(style)

    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
    x = np.linspace(-13, 13, 150)

    # Set seed values to replicate results of random draws
    np.random.seed(9)

    for i in range(3):

        # Draw mean and standard deviation from uniform distributions
        m, s = np.random.uniform(-8, 8), np.random.uniform(2, 2.5)

        # Generate a normal density plot
        y = norm.pdf(x, loc=m, scale=s)
        axes[0].plot(x, y, linewidth=3, alpha=0.7)

        # Create a scatter plot with random X and Y values 
        # from normal distributions
        rnormX = norm.rvs(loc=m, scale=s, size=150)
        rnormY = norm.rvs(loc=m, scale=s, size=150)
        axes[1].plot(rnormX, rnormY, ls='none', marker='o', alpha=0.7)

        # Create a histogram with random X values
        axes[2].hist(rnormX, alpha=0.7)

        # and a line graph with random Y values
        axes[3].plot(x, rnormY, linewidth=2, alpha=0.7)

    style_name = style.split('-')[0]
    plt.suptitle(f'Style: {style_name}', fontsize=13)
    plt.show()

```

ചില styles എങ്ങനെയാണ് കാണപ്പെടുന്നത് എന്ന് നോക്കാം.

ആദ്യം, `seaborn` എന്ന style sheet ഉപയോഗിച്ച് graphs വരയ്ക്കാം

```{code-cell} python3
draw_graphs(style='seaborn-v0_8')
```

plots-ലെ colors നീക്കം ചെയ്യാൻ നമുക്ക് `grayscale` ഉപയോഗിക്കാം

```{code-cell} python3
draw_graphs(style='grayscale')
```

`ggplot` എങ്ങനെയാണ് കാണപ്പെടുന്നത് എന്നത് ഇതാ

```{code-cell} python3
draw_graphs(style='ggplot')
```

`dark_background` എന്ന style-ഉം നമുക്ക് ഉപയോഗിക്കാം

```{code-cell} python3
draw_graphs(style='dark_background')
```

list-ലെ മറ്റ് styles പരീക്ഷിക്കാൻ ഈ function നിങ്ങൾക്ക് ഉപയോഗിക്കാം.

താൽപ്പര്യമുണ്ടെങ്കിൽ, നിങ്ങളുടെ സ്വന്തം style sheets തന്നെ create ചെയ്യാവുന്നതാണ്.

നിങ്ങളുടെ style sheets-നുള്ള Parameters `plt.rcParams` എന്ന dictionary പോലുള്ള variable-ൽ store ചെയ്യപ്പെടുന്നു

```{code-cell} python3
---
tags: [hide-output]
---
 
print(plt.rcParams.keys())

```

നിങ്ങളുടെ style sheets-ന് set ചെയ്യാവുന്ന ധാരാളം parameters ഉണ്ട്.

നിങ്ങളുടെ style sheet-ന് parameters set ചെയ്യുക: 

1. നിങ്ങളുടെ സ്വന്തം [`matplotlibrc` file](https://matplotlib.org/stable/users/explain/customizing.html) create ചെയ്തുകൊണ്ട്, അല്ലെങ്കിൽ
2. `plt.rcParams` എന്ന dictionary പോലുള്ള variable-ൽ store ചെയ്ത values update ചെയ്തുകൊണ്ട്

രണ്ടാമത്തെ method ഉപയോഗിച്ച് overlaid ആയ density lines-ന്റെ style മാറ്റാം

```{code-cell} python3
from cycler import cycler

# set to the default style sheet
plt.style.use('default')

# You can update single values using keys:

# Set the font style to italic
plt.rcParams['font.style'] = 'italic'

# Update linewidth
plt.rcParams['lines.linewidth'] = 2


# You can also update many values at once using the update() method:

parameters = {

    # Change default figure size
    'figure.figsize': (5, 4),

    # Add horizontal grid lines
    'axes.grid': True,
    'axes.grid.axis': 'y',

    # Update colors for density lines
    'axes.prop_cycle': cycler('color', 
                            ['dimgray', 'slategrey', 'darkgray'])
}

plt.rcParams.update(parameters)


```

```{note} 

ഈ settings `global` ആണ്. 

`.rcParams`-ലെ parameters മാറ്റിയ ശേഷം generate ചെയ്യുന്ന ഏതൊരു plot-ഉം ഈ setting-ന്റെ ബാധ്യതയിലായിരിക്കും.

```

```{code-cell} python3
fig, ax = plt.subplots()
x = np.linspace(-4, 4, 150)
for i in range(3):
    m, s = uniform(-1, 1), uniform(1, 2)
    y = norm.pdf(x, loc=m, scale=s)
    current_label = rf'$\mu = {m:.2}$'
    ax.plot(x, y, linewidth=2, alpha=0.6, label=current_label)
ax.legend()
plt.show()
```

നിങ്ങളുടെ style വീണ്ടും default ആയി മാറ്റാൻ `default` style sheet വീണ്ടും apply ചെയ്യുക

```{code-cell} python3

plt.style.use('default')

# Reset default figure size
plt.rcParams['figure.figsize'] = (10, 6)

```

## Further Reading

* [Matplotlib gallery](https://matplotlib.org/stable/gallery/index.html) ധാരാളം examples നൽകുന്നു.
* Nicolas Rougier, Mike Muller, Gael Varoquaux എന്നിവരുടെ ഒരു നല്ല [Matplotlib tutorial](https://scipy-lectures.org/intro/matplotlib/index.html).
* [mpltools](https://tonysyu.github.io/mpltools/index.html) plot styles-ന്റെ ഇടയിൽ എളുപ്പത്തിൽ switch ചെയ്യാൻ അനുവദിക്കുന്നു.
* [Seaborn](https://github.com/mwaskom/seaborn) Matplotlib-ൽ common ആയ statistics plots സുഗമമാക്കുന്നു.

## Exercises

```{exercise-start}
:label: mpl_ex1
```

function plot ചെയ്യുക

$$
f(x) = \cos(\pi \theta x) \exp(-x)
$$

`np.linspace(0, 2, 10)`-ലെ ഓരോ $\theta$-ക്കും $[0, 5]$ എന്ന interval-ൽ.

എല്ലാ curves-ഉം ഒരേ figure-ൽ വയ്ക്കുക.

output ഇതുപോലെ കാണപ്പെടണം

```{image} /_static/lecture_specific/matplotlib/matplotlib_ex1.png
:scale: 130
:align: center
```

```{exercise-end}
```

```{solution-start} mpl_ex1
:class: dropdown
```

ഇതാ ഒരു solution

```{code-cell} ipython3
def f(x, θ):
    return np.cos(np.pi * θ * x ) * np.exp(- x)

θ_vals = np.linspace(0, 2, 10)
x = np.linspace(0, 5, 200)
fig, ax = plt.subplots()

for θ in θ_vals:
    ax.plot(x, f(x, θ))

plt.show()
```

```{solution-end}
```