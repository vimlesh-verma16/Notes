// learn js at mdn webdocs javascrip


// var digit1 = 5, x = 1, z;
// z = digit1 + x;
// alert(z);

// let a = 1;  
// const x = 3;
// a = 2;
// x=5;
// a++;
// console.log(a++);
// console.log(a++);
// console.log(x);  

// let x=5,y="4"; //number,string
// console.log(x+y); //string


// let x="hello",y="world";
// console.log(x+" "+y); //string
// console.log(`${x} vimlesh`); //template literal with string  

//it is used to know data type of variable.
// let x = "hello", y = 1;
// console.log(typeof x, typeof y);


// ---------------------------------------

//conditinal operator if-else

// let age = 19;
// let hasvoterid = "yes";
// if (age >= 18 && hasvoterid == "yes") {
//     alert("you can vote")
// }
// else if (age > 18 && hasvoterid != "yes") {
//     alert("get your voter id")
// }
// else {
//     alert("you cnnot vote")
// }


//nested if else

// let age = 19;
// let hasvoterid = "yes";
// if (age >= 18) {
//     if (hasvoterid == "yes") {
//         alert("you can vote");
//     }
//     else {
//         alert("you cannot vote")
//     };

// }

// -------------------------------------
// ternary operator 
  
// let loggedin= 0; //- 0 for loggedout 1 for loggedin

// let option = loggedin == 1 ? "logout" : "login";
// alert(option);

// -----------------------------------
// question- if input= 1,"y,"yes" ouput="continue" 
//if input - 0,"n","no" output="end"

 
// let input = "n";

// if (input === 1 || input === "y" || input === "yes") {
//     document.write("continue"); 
// }

// -------------- --------------------

//  switch case  with 'same problem' 
// let input = "1";

// switch (input) {  

//     case 1:
//         document.write("continue")
//         break;
//     case "y":
//         document.write("continue")
//         break;
//     case "yes":
//         document.write("continue")
//         break;
//     case 0:
//         document.write("end")
//         break;
//     case "n":
//         document.write("end")
//         break;
//     case "no":
//         document.write("end")
//         break;
//     default:
//         document.write("wrong hello");
// }

// ---------------------------------------------------------------------

//use of while and do while etc 

// let counter = 0;
// while(counter <=5){
//     document.write("techgun");
//   counter++;
// }

// let x=0;
// sum=0;;

//sum of even number
// while(x<=3){
//     if(x%2==0){
//         sum=sum+x;
//     }
//     x++;

// }
// document.write(sum);

// ----------------------------

// DO WHILE LOOP

// let counter=3;
// do{
//     document.write("hello world");
//     counter++;
// }while(counter<=10);

// ------------------------------------------------------

// For LOOP

// for(let counter=0;counter<=2;counter++){
//     document.write("hello");

// }

// -----------------------------------------------------------------------------
// break continue 


// for(let counter=0;counter<=9;counter++){
//     if(counter==4){
//         break;
//     }
//     document.write(counter);
//     document.write("<br>")
// };

// for(let counter=1;counter<=10;counter++){
//     if(counter==4){
//         continue;
//     }
//     document.write(counter);
//     document.write("<br>")
// };

// ----------------------------------------------------------------------------

//nested for loop 

// outer: for (let counter = 0; counter <= 9; counter++) {

//     document.write(counter);
//     document.write("<br>")

//     for (let counter2 = 1; counter2 < 3; counter2++) {
//          if(counter==3){
//              break outer;
//          }

//         document.write("techgun")
//         document.write("<br>")
//     };

// };

// -----------------------------------------------------------------------------

//prompt 

// let a = prompt("enter age", 20)
// if (a != null) {
//     document.write("your age is  :");

//     document.write(a);
// }
// else {
//     document.write("age field was blank ");
// }

// -----------------------------------------------------------------------------

//confirm

// let response = confirm("are you sure,you want to delete");

// if(response){
//     document.write("deleted");

// }
// else{
//   document.write("Not deleted");
// }

// -----------------------------------

//type conversion
  
// let type="5"-2;
// console.log(type);
// console.log(typeof type);

// let type = "22";
// console.log(typeof type);//old
// let newtype = Number(type);
// console.log(typeof newtype);//new


// let type = true;
// console.log(typeof type);//old
// let newtype = String(type);
// console.log(typeof newtype);//new

// -----------------------------------------------------------------------------------------------

// string manipulations -- concat ,indexof , str.length,str.substr,str.substring ,str.lastIndexOf

// let str = "vimlesh";
// let greet = `hello ${str}`;
// console.log(greet);
 
// let str = "vimlesh\"verma";
// // console.log(str);
// console.log(str.length);
// console.log(str[2]);

// let str = "vishwajeet";
// let str2 = "kumar";
// let str3 = str.concat("   ", str2);
// console.log(str3);


// let str = "this is javascript tutorial written by vimlesh verma  ";
// let str1=str.substr(8,19); //used to find substring with start as 8 and then find 19 lenght string
// console.log(str1)
// let str2=str.substring(8,17); //used to find substring with start as 8 and end with 17
// console.log(str2)
// let position =str.indexOf("by"); //in this search from start
// let position =str.lastIndexOf("hello"); //search from last
// console.log(position);

// #--------------------------------------------------------------------------------------------

// removing white space:- str.trim,str.toLowerCase(),trimstart ,trimend,str.replace,toUpperCase(),str.replace,includes

// let str = "  this is javascript tutorial is written by vimlesh verma  ";
// let trimedstr = str.trim()  //trimstart ,trimend.
// let trimedstr = str.toLowerCase();//UpperCase

// let trimedstr = str.replace(" is ", " is the best ");
// console.log(str);
// console.log(trimedstr);

// let tri=str.includes("iswq")
// console.log(tri) //it is boolean which writtens true if it contains

// -----------------------------------------------------------------------------------------

// # ARRAY

// let book = ["math", "physics", "chemistry", "bio"];

// let book = new Array("math", "physics", "chemistry", "bio");
// book[1] = "computer science"; 

// console.log(book);

// operations on array;

// console.log(book.length);
// book.push("hindi");//insert an element at the last. 
// book.unshift("hindi");// inserting an element at the first;
// book.pop();//removing an element from the last ;
// book.shift(); //remove from the front.
// console.log(book);

// book.splice(1, 2); //used to remove specific element fron array;
// console.log(book);
// book = [];//used for emptying the array
// book.length = 0;
// let position = book.indexOf("bio");
// console.log(position);

// let text = "this is a random text";
// let wordarray=text.split(' ');
// console.log(wordarray);

// let book = ["math", "physics", "chemistry", "bio"];
// let book2 = ["hindi", "english"];
// let book3 = ["pe", "drawing"];
// let wordarray = book.join(" ");

// let newbook = book.concat(book2,book3);
// console.log(newbook);

// ----------------------------------------------------------------------------------------

//# MULTIDIMENSIONAL ARRAY
// let book = ["math", "physics", "chemistry", "bio"];

// let bookwithpages = [
//     ["maths", "200"],
//     ["bio", "100"],
//     ["phy", "344"]
// ];
// console.log(bookwithpages[1][0]);

//accessing array with for loop

// let book = ["math", "physics", "chemistry", "bio"];

// let booklength = book.length;
// for (i = 0; i < booklength; i++){
//     console.log(`element ${i} is ${book[i]}`);
// }

// --------------------------------------------------------------------------------------------------accessing with for each

// let book = ["math", "physics", "chemistry", "bio"];
// book.forEach(myfu);
// function myfu(value) {
//     console.log(value);
// }

// -----------------------------------------------------------------------------------------------------------

//#  FUNCTIONs

// function Multable(num) {

//     for (i = 1; i <= 10; i++) {
//         document.write(`${num} X ${i} = ${num * i}`);
//         document.write("<br>");
//     }
//     document.write("<br>");
// }

// Multable(10);
// document.write("hello <br><br>");
// Multable(25);

//ADDTION FUNCTION  
// function add(num1,num2){
//   document.write(num1+num2);
//   document.write("<br>");
// }
// add(2,4);
// add(2,8); 
// add(2,10);

// function add() {
//     if (arguments.length == 0) {
//         console.log("no arguments were passed !");
//     }
//     else {
//         let sum = 0;
//         for (let i = 0; i < arguments.length; i++) {
//             sum = sum + arguments[i];
//         }
//         console.log(sum);
//     }

// }
// let addition=add;
// add(1,2);
// addition(5,5);


// # RETURN FUNCTION
// function compare(a,b) {
//    if(a>b){
//        return 1;
//    }
//    else{
//        return 0;
//    }
// }
// let c = compare(4, 6);
// document.write(c);

// ------------------------------------------------------------------------------------------------

//# GLOBAL VARIABLE VS LOCAL VARIABLE

// let car="audi"; //GLOBAL VARIABLE can used any where 

// function add(){
//     let result =30; //  LOCAL VARIABLE can be used inside only the function only
//     console.log(result);
//     console.log(car);
// }

// add();

// ----------------------------------------------------------------------------------------

//#ANONYMOUS FUNCTIONS

//function expressio0n
// let show =function (){
//     console.log("hello world !")
// };
// show();

// setTimeout(show,3000);//it show function after 3sec delay;

// ---------------------------------------------------------------------------------------

// setTimeout(function (){
//     console.log("hello world !")
// },3000); //Another method to write it .


// -----------------------------------------------------------------------------------------

//# IMMEDIATELY INVOKED FUNCTION
// ( function () {
//     console.log("hello world");
//     alert("hello world");
// })();


// ------------------------------------------------------------------------------------

// # OBJECT 

// let person = {
//     firstName: 'vimlesh',
//     lastname: 'verma'
// };


// person.age =22; // adding property
// person.firstName="vimmu";
// console.log(person.firstName);//dot notation
// console.log(person['lastname']);// ARRAY Like notation
// delete person.lastname ;//deleting property 
// console.log('age' in person); 

// -----------------------------------------------------------------------------------

// iterating properties of object  with  #FOR IN LOOP
// for(let key in person){
//     // console.log(key);
//     console.log(key +":"+person[key]);
// } 


// let person = {
//     firstName: 'vimlesh',
//     lastname: 'verma',
//     sayHello:function greet() {
//             console.log("hello!");
//         }
// };

// person.sayHello=function(){
//     console.log("hello !")
// }
// person.sayHello();

// -----------------

// function greet() {
//     console.log("hello! greet");
// }
// person.sayHello = greet();
// person.sayHello;


// # THIS --------------------------------------------------------------------------------

// let person = {
//     firstName: 'vimlesh',
//     lastname: 'verma',
//     sayHello:function greet() {
//             console.log("hello! i am "+this.firstName + " and i have " + car.brand +" car" );
//         }
// };


// let car={
//     brand :"tata",
//     model:"nexon",
// }
// person.sayHello();

// -------------------------------------------------------------------------------------

// # GENERATING A RANDOM NUMBER 

// let x = Math.ceil(Math.random()*10);

//let x = Math.floor(Math.random() * (25 - 15)) + 15; //generating any number between 24 to 15 .
// console.log(x);

// function getRandom(min,max) {
//     let x = Math.floor(Math.random() * (max - min+1)) + min;
//     return x;
// }
// console.log(getRandom(5, 10));

// -------------------------------------------------------------------------------------

//# DATE OBJECT 
//new Date(year,month,day,hour,min,sec) 

// let x = new Date(2020,10,11,1,22,2);
// console.log(x.getFullYear(),x.getMonth(),x.getHours());
// x.setDate(x.getDate()+9);
// console.log(x);
// ---------------------------------------------------------------------------------------
//  # GETTERS AND SETTERS

// let person = {
//     name: "vimlesh verma",
//     age: 22,

    // getname: function () {
    //     return this.name.toUpperCase(); //method 1
    // }

  // get getname(){
  //     return this.name.toUpperCase(); //method 2
  // },

//     set setname(n) {
//         this.name = n.toUpperCase();
//     }

// };
// console.log(person.getname());//method 1  get function
// console.log(person.getname);//method 2

// person.setname = "verma";  // set function 
// console.log(person);  

// -------------------------------------------------------------------------------

// # OBJECT CONSTRUCTOR FUNCTION 

// function Student(first, last, age, cls) {
//     this.firstname = first;
//     this.lastname = last;
//     this.age = age;
//     this.cls = cls;
    // this.nationality = "india";
// }

// var student1 = new Student("vimmu", "verma", 22, 10);  
// var student2 = new Student("vimlesh", "verma", 2, 23);
// var student3 = new Student("vishwajeet","verma",3,3);

// student1.name = function () {
//     return this.firstname + " " + this.lastname;
// } 


// console.log(student1);
// console.log(student1.name());
// console.log(student2);
// console.log(student3);

// ----------------------------------------------------------------------------

//  #  PROTOTYPE 
// Student.prototype.nationality="indian";
// Student.prototype.name = function () {
//     return this.firstname + " " + this.lastname;
// }
// console.log(student1.name());


// -------------------------------------------------------------------------------

// # NESTED OBJECT 

// var user = {
//     id: 101,
//     email:"vimleshverma@gmail.con",
//     personalinfo:{
//         name: "vimmu",
//         address:{
//             street:"dsdfsa",
//             city:"khandwa",
//             country:"india",
//         }
//     }
// };

// console.log(user);
// console.log(user.personalinfo);
// console.log(user.personalinfo.address);

// -------------------------------------------------------------------------------

// # HOISTING  it puts all the  declaration at the begining  or in the scope of local variable;
// x=7;
// console.log(x);
// var x;

// ------------------------------------------------------------------------------

// ## DOCUMENT OBJECT MODEL (DOM) . 































































