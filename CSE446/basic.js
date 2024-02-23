// const a=2
// const b=3

// function rand(a,b, sum){
//     const total = a+b*sum
//     return total

// }

// console.log (rand(1,2,5))


// var array= [1,2,3]

// array.push(4)

// console.log(array)
// array.pop(4)

// console.log(array)
// array.shift()
// console.log(array)
// array.unshift('heda')
// console.log(array)
// console.log(array.length)

// array.forEach(function (element){
//     console.log(element)
// })


// Sample array
// const myArray = [1, 2, 3, 4, 5];

// // Using forEach to print each element
// myArray.forEach(function(element) {
//   console.log(element);
// });


// const array= ['z','a','w','a','d']
// var sum=''

// array.forEach(function(element){
//     if (element!=='a' && element!=='d'){
//         console.log(element)}
    
// })

const obj={
    a:5,
    b:3,
    c:3
}

for (const property in obj){
    console.log(obj[property])
}