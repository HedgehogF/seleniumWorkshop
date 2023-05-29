# SELECTORS

### Note: Structure of a html element
![img](../resources/grumpy-cat-small.png)

![img2](../resources/grumpy-cat-attribute-small.png)
## XPATH

**XPath** provides various selection mechanisms to locate elements in an XML or HTML document. Here are some commonly used XPath selection methods:

- Selecting elements by tag name:

  - Example: `//tagname` selects all elements with the specified tag name.

- Selecting elements by attribute:

  - Example: `//tagname[@attribute='value']` selects elements with the specified attribute value.

- Selecting elements by attribute presence:

  - Example: `//tagname[@attribute]` selects elements that have the specified attribute.

- Selecting elements by attribute partial match:

  - Example: `//tagname[contains(@attribute, 'value')]` selects elements where the attribute contains the specified value.

- Selecting elements by text content:

  - Example: `//tagname[text()='value']` selects elements with the specified text content.

- Selecting elements by position:

  - Example: `(//tagname)[position()]` selects the element at the specified position. The index starts from 1.

- Selecting elements based on the relationship with other elements:

  - Example: `//parenttagname/childtagname` selects child elements that are direct children of parent elements.

- Selecting elements based on multiple criteria:

  - Example: `//tagname[@attribute='value' and @attribute2='value2']` selects elements that satisfy multiple attribute conditions.

- Selecting elements using wildcard:

  - Example: `//tagname[contains(@attribute, 'value*')]` selects elements where the attribute starts with "value" followed by any characters.

## CSS

1. **Selecting elements by tag name**:
   ```css
   tagname
   ```
   This selects all elements with the specified tag name.

2. **Selecting elements by attribute**:
   ```css
   tagname[attribute='value']
   ```
   This selects elements with the specified attribute value.

3. **Selecting elements by attribute presence**:
   ```css
   tagname[attribute]
   ```
   This selects elements that have the specified attribute.

4. **Selecting elements by attribute partial match**:
   ```css
   tagname[attribute*='value']
   ```
   This selects elements where the attribute contains the specified value.

5. **Selecting elements by position**:
   ```css
   tagname:nth-child(position)
   ```
   This selects the element at the specified position. The index starts from 1.

6. **Selecting elements based on the relationship with other elements**:
   ```css
   parenttagname > childtagname
   ```
   This selects child elements that are direct children of parent elements.

7. **Selecting elements based on multiple criteria**:
   ```css
   tagname[attribute='value'][attribute2='value2']
   ```
   This selects elements that satisfy multiple attribute conditions.

8. **Selecting elements using wildcard**:
   ```css
   tagname[attribute^='value']
   ```
   This selects elements where the attribute starts with "value" followed by any characters.

