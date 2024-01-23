/*Crie um programa que seja capaz de percorrer uma lista de números e imprima cada número Par encontrado.*/

const array = [];

array.push(1);
array.push(2);
array.push(3);
array.push(4);
array.push(5);
array.push(6);
array.push(7);
array.push(8);
array.push(9);
array.push(10);

for(let i=0; i<array.length; i++){
    if(array[i] % 2 == 0) console.log(array[i]);
}