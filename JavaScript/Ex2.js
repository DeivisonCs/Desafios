/*
    - Crie uma classe para representar pessoas;
    - Deve possuir nome, peso e altura;
    - Deve dizer o valor do IMC (peso / (altura * altura));
    - Instancie uma pessoa chamada Jose que tem 70Kg de peso e 1,75 de altura, e peça o valor do seu IMC;
*/

class Person{
    name;
    height;
    weight;

    constructor(name, height, weight){
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    get_IMC(){
        return this.weight / (this.height * this.height);
    }

}

const jose = new Person("José", 1.75, 70);

console.log(jose.get_IMC());

