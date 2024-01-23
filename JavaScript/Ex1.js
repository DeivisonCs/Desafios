/*  - Crie uma classe para representar carros;
    - Devem possuir marca, cor e gasto médio por kilometro;
    - Crie um método que dado a quantidade de km e o preço do combustível, retorne o valor gasto em reais para realizar o percurso. 
*/

class Car {
    marca;
    cor;
    gastoPorKm;

    constructor(marca, cor, gkm){
        this.marca = marca;
        this.cor = cor;
        this.gastoPorKm = gkm;
    }

    calcular_Custo_Do_Percurso(distancia, precoCombustivel){
        return distancia * this.gastoPorKm * precoCombustivel;
    }
}

const MyCar = new Car('Mustang', 'Preto', 1/5);

console.log(MyCar.calcular_Custo_Do_Percurso(70, 5.9));