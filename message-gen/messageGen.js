let quotes = [
    "Start where you are. Use what you have. Do what you can.", 
    "I never dreamed about success. I worked for it.", 
    "I am deliberate and afraid of nothing.", 
    "You can\'t use up creativity. The more you use, the more you have.", 
    "Sometimes, you\'ve got to work a little, so you can ball a lot."
]

let food = [
    "burgers",
    "fries",
    "tacos",
    "cereals",
    "rice"
]

let timeOfDay =[
    "morning",
    "evening",
    "afternoon",
    "night",
    "noon"
]

let animals = [
    "dogs",
    "cats",
    "lions",
    "kangaroos",
    "monkeys"
]

let sentenceStarters = [
    "My favorite animals are",
    "My favorite foods are",
    "Heres an inspirational quote:  "
]

function randomNum(){
   return Math.floor(Math.random() * 5);
}


function generateMessage(){
    let i = Math.floor(Math.random() * 3);
    if(i === 0){
        console.log(`${sentenceStarters[i]} ${animals[randomNum()]}. I would love one as a pet`);
    }
    if(i === 1){
        console.log(`${sentenceStarters[i]} ${food[randomNum()]}. I like eating them during the ${timeOfDay[randomNum()]}`);
    }
    if(i === 2){
        console.log(`${sentenceStarters[i]}${quotes[randomNum()]}`);
    }
}

generateMessage();


