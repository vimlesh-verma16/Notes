## All- Notes

https://github.com/vimlesh-verma16/Notes/wiki

### MVT VS MVC 

### **Difference Between MVC and MVT**

| Feature         | MVC (Model-View-Controller)    | MVT (Model-View-Template)  |
|--------------- |--------------------------------|----------------------------|
| **Architecture** | Divides application into **Model**, **View**, and **Controller**. | Divides application into **Model**, **View**, and **Template**. |
| **Control Flow** | The **Controller** handles user input and updates the Model & View accordingly. | The **framework (like Django) acts as the Controller**, handling data flow between the Model and the Template. |
| **Role of Developer** | Developer needs to write the Controller logic explicitly. | Django handles most of the controller logic automatically. |
| **View Handling** | View retrieves data from the Model and applies logic before rendering it. | Template is responsible for rendering dynamic content using Django’s template language. |
| **Example Frameworks** | **Spring MVC (Java), Laravel (PHP), Ruby on Rails (Ruby)** | **Django (Python)** |

### **Key Takeaways:**
- **MVC** is a **general pattern** used across multiple frameworks and languages.
- **MVT** is **Django-specific** and abstracts the Controller layer, making development easier.
