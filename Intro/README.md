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


## Exceptions

1. **NoSuchElementException**: This exception is raised when an element cannot be found on the page.
    
2. **TimeoutException**: This exception is raised when a command exceeds the maximum time allowed for execution.
    Code which causes the TimeoutException :
```
    WebDriverWait wait = new WebDriverWait(driver, 30);
    WebElement idElement;
    idElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("123")));
```

3. **StaleElementReferenceException**: This exception is raised when a referenced element is no longer attached to the DOM.
4. **ElementNotVisibleException**: This exception is raised when an element is present in the DOM but not visible to the user.
    Code which causes the ElementNotVisibleException :
```
    <input type='button' hidden=true value='save'>
    
    // click the button which is hidden (not visible)
    driver.find_element_by_xpath("//input[@type='button']")).click();
```
5. **ElementNotInteractableException**: This exception is raised when an element is present in the DOM but not interactable, such as being disabled.

    Code which causes the InvalidElementStateException :
    ```
    <input type='button' disabled=true value='save'>
    
    // click the button which is disabled
    driver.find_element_by_xpath("//input[@type='button']")).click();
    ```
6. **NoSuchFrameException**: This exception is raised when a frame or iframe cannot be found.
    Code which causes the NoSuchFrameException :
    ```
    driver.switch_to_frame("frame1");
    ```
7. **NoSuchWindowException**: This exception is raised when a window or tab cannot be found.
   Code which causes the NoSuchWindowException :
    ```
    driver.switch_to_window("window Gu ID")
    ```
8. **InvalidSelectorException**: This exception is raised when an invalid selector is used in a WebDriver command.
9. **UnexpectedAlertPresentException**: This exception is raised when an unexpected alert is present on the page.
10. **WebDriverException**: This is a general exception that serves as the base class for all other Selenium exceptions.

Notes: All exceptions supported in python. [Doc](https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html#module-selenium.common.exceptions)
