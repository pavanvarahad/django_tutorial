# 1. HTML Fundamentals

HTML (HyperText Markup Language) is the standard language used to create the structure of web pages. It is not a programming language in the sense that it does not handle logic or calculations; instead, it is a markup language that tells the browser how to organize and display content. Understanding HTML is the first and most essential step in web development.

---

### What HTML Is and How the Browser Parses It

HTML acts as the skeleton of a website. It uses a system of "markup" to annotate text, images, and other media so the browser understands their purpose—whether something is a heading, a paragraph, or a link.

**Parsing** is the process where a web browser reads your HTML code and converts it into a visual webpage. The browser reads the file from top to bottom, creating a "map" of the document known as the **DOM (Document Object Model)**. If the HTML is the blueprint, the DOM is the actual framework the browser uses to render the pixels on your screen.

### HTML Versions and Living Standard Concept

In the early days of the web, HTML was released in version increments (such as HTML 4.01 or XHTML). However, this meant that the language only improved every few years.

Today, HTML is managed as a **Living Standard** by the WHATWG (Web Hypertext Application Technology Working Group). This means that HTML is no longer a "versioned" language. Instead, it is a continuously evolving specification. Features are added or refined as technology changes, ensuring that the web stays modern without needing a "HTML 6."

### Anatomy of an HTML Document

A standard HTML file follows a strict, nested hierarchy. Each part of the "anatomy" serves a specific purpose:

1.  **The Root Element (`<html>`):** The container for everything else in the document.
2.  **The Head (`<head>`):** Contains metadata (data about the data) that isn't visible to the user, such as the page title, character encoding, and links to CSS files.
3.  **The Body (`<body>`):** Contains all the content that users actually see, such as text, images, and buttons.

### Doctype and Standards Mode

The very first line of an HTML document must be the **Doctype declaration**:

```html
<!DOCTYPE html>
```

The Doctype is not an HTML tag; it is a preamble that tells the browser which version of HTML the page is using. By using `<!DOCTYPE html>`, you trigger **Standards Mode**. This ensures the browser follows modern web specifications. If the Doctype is missing, browsers may enter "Quirks Mode," where they try to emulate older, buggy rendering engines from the 1990s, which often breaks modern layouts.

### HTML Syntax Rules

To ensure browsers parse code correctly, developers must follow specific syntax rules:

*   **Tags:** Keywords surrounded by angle brackets, such as `<p>`.
*   **Opening and Closing:** Most elements require an opening tag (`<p>`) and a closing tag (`</p>`) that includes a forward slash.
*   **Nesting:** Elements must be closed in the reverse order they were opened. For example:
    *   Correct: `<p><strong>Bold text</strong></p>`
    *   Incorrect: `<p><strong>Bold text</p></strong>`
*   **Case Sensitivity:** While HTML tags are case-insensitive (`<DIV>` is the same as `<div>`), the industry standard is to always use lowercase.

### Elements vs Attributes

While these terms are often used interchangeably, they represent different parts of the code:

*   **Element:** The entire unit, from the opening tag to the closing tag, including the content inside.
*   **Attribute:** Special words placed inside the opening tag to provide additional information or behavior. Attributes usually come in name/value pairs.

```html
<!-- The whole line is an element -->
<a href="https://google.com">Click Here</a>

<!-- 'href' is the attribute name, the URL is the attribute value -->
```

### Void Elements

Most elements contain content (like text or other tags), but **Void Elements** do not. Because they have no content, they do not require a closing tag. Some common void elements include:

*   `<img>` (Image)
*   `<br>` (Line break)
*   `<hr>` (Horizontal rule)
*   `<input>` (Form input)

In modern HTML, you can write them as `<img>` or `<img />`. Both are technically correct, though the first is more common in HTML5.

### Block vs Inline Elements

The browser categorizes elements based on how they sit on the page:

1.  **Block-level Elements:** These always start on a new line and take up the full width available. They act as "containers" or "blocks." Examples include `<div>`, `<h1>` through `<h6>`, and `<p>`.
2.  **Inline Elements:** These do not start on a new line. They only take up as much width as their content requires and sit side-by-side with other inline elements. Examples include `<span>`, `<a>`, and `<strong>`.

### HTML Comments

Comments are notes left for the developer that the browser ignores entirely. They are useful for documenting why a certain piece of code exists or for organizing long files.

**Syntax:**
```html
<!-- This is a comment. It will not show up on the website. -->

<p>This text will be visible.</p>

<!-- 
    Comments can also
    span multiple lines.
-->
```