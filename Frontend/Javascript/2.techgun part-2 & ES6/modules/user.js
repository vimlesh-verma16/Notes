import { withdraw as act} from "./account.js";

export default function(){
    console.log("this is user defalt function called..")
}




export let name="vimlesh";
export let age=22;

export function code(){
    console.log("coding...");
    act();
}

function cook(){
    console.log("cooking");
}

export function withdraw(){
    console.log("user function widthdraw called a...");
}