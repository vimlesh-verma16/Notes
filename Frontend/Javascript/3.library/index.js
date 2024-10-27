console.log("this is our js ");

// constructor
function Book(name, author, type) {
    this.name = name;
    this.author = author;
    this.type = type;
}

// Display constructor
function Display() {

}
//add methods to display protype
Display.prototype.add = function (book) {
    console.log("adding to UI");
    tablebody = document.getElementById("tablebody");
    let uistring = ` 
    <tr>
         <td>${book.name}</td>
        <td>${book.author}</td>
        <td>${book.type}</td>
    </tr>`;

    tablebody.innerHTML += uistring;

}
//impliment the clear function
Display.prototype.clear = function () {
    let libraryForm = document.getElementById("libraryForm");
    libraryForm.reset();
}
//impliment the validate function 
Display.prototype.validate = function (book) {
    if (book.name.length < 2 || book.author.length < 2) {
        return false;
    }
    else {
        return true;
    }
}
Display.prototype.show = function (type, dmessage) {
     let a= document.getElementById("alert");
    a.innerHTML = `<div class="alert alert-${type} alert-dismissible fade show" role="alert">
    <strong>message:</strong>${dmessage}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>`;
}

//add submit event listener 
let libraryForm = document.getElementById("libraryForm");
libraryForm.addEventListener("submit", libraryFormSubmit);

function libraryFormSubmit(e) {
    console.log("you hava submitted form");
    let name = document.getElementById("name").value;
    let author = document.getElementById("author").value;
    let type;

    let fiction = document.getElementById("Fiction");
    let programming = document.getElementById("Programming");
    let novel = document.getElementById("Novel");

    if (fiction.checked) {
        type = fiction.value;
    }
    else if (programming.checked) {
        type = programming.value;
    }
    else if (novel.checked) {
        type = novel.value;
    }

    let book = new Book(name, author, type);
    console.log(book);
    let display = new Display();
    if (display.validate(book)) {
        display.add(book);
        display.clear(book);
        display.show("success", "  your book is succsfully submit")
    }
    else {
        display.show("danger", "  SOrry You cannot add this book");
    }

    e.preventDefault();
}