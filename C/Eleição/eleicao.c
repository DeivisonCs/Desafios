#include <stdio.h>
#include <stdlib.h>

#define MAX 20
#define candidatos 3    //Total de candidatos a cadastrar

struct prefeito{
    
    char nome[MAX], partido[MAX];
    int  num, totalVotos;
    float percentual_votos;
};

struct vereador{
    
    char nome[MAX], partido[MAX];
    int  num, totalVotos;
    float percentual_votos;
};

struct prefeito pref[candidatos];
struct vereador ver[candidatos];

int main()
{
    int voto, votosNulos[2]={0, 0}, total_votos[2];  //0-Prefeito  1-Vereador
    char confirm=' ';
    float percent_nulos[2];
    int C, ctrl=0, aux; //variáveis de controle/auxiliares

//Cadastro dos Candidatos
for(C=0; C<candidatos; C++)
{
    printf("Cadastro Prefeitos: \n");
    printf("Nome: ");
    gets(pref[C].nome); fflush(stdin);
    printf("Numero: ");
    scanf("%d", &pref[C].num); fflush(stdin);
    printf("Partido: ");
    gets(pref[C].partido); fflush(stdin);
    pref[C].totalVotos = 0;
system("cls");
}

for(C=0; C<candidatos; C++)
{
    printf("Cadastro Vereadores: \n");
    printf("Nome: ");
    gets(ver[C].nome); fflush(stdin);
    printf("Numero: ");
    scanf("%d", &ver[C].num); fflush(stdin);
    printf("Partido: ");
    gets(ver[C].partido); fflush(stdin);
    ver[C].totalVotos = 0;
system("cls");
}

    //Voto Prefeito
    do{
    system("cls");
        printf("Voto para Prefeito: ");
        scanf("%d", &voto); fflush(stdin);

        if(voto < 0){
            ctrl = 1;
            break;
        }

        for(C=0, ctrl=0; C<candidatos; C++)
        {
        //confirmação das credenciais do candidato
            if(voto == 0){
                printf("\nVoto Nulo!");
                break;
            }else if(voto == pref[C].num) 
            {
                printf("\nNome: %s", pref[C].nome);
                printf("\nNumero: %d", pref[C].num);
                printf("\nPartido: %s", pref[C].partido);
                break;
            }
            if(C+1 == candidatos)   //caso não tenha candidato correspondente
            ctrl = 2;
        }
        if(ctrl == 2)
        continue;
        

        printf("\nConfirmar Voto (C-confirmar / D-corrigir): ");
        scanf(" %c", &confirm); fflush(stdin);

        if(confirm == 'C' || confirm == 'c')
        {
        //Soma do voto feito
            for(C=0; C<candidatos; C++)
            {
                if(voto == 0){
                    votosNulos[0]++;
                    break;
                }else if(voto == pref[C].num){
                    pref[C].totalVotos++;
                    break;
                }
            }
        }
    }while(confirm != 'C' && confirm != 'c');
    confirm=' ';

//Voto Vereador
if(ctrl != 1)
{
    while(confirm != 'C' && confirm != 'c'){
    system("cls");
        printf("Voto para Vereador: ");
        scanf("%d", &voto); fflush(stdin);

        for(C=0, ctrl=0; C<candidatos; C++)
        {
            //confirmação das credenciais do candidato
            if(voto == 0){
                printf("\nVoto Nulo!");
                break;
            }else if(voto == ver[C].num)
            {
                printf("\nNome: %s", ver[C].nome);
                printf("\nNumero: %d", ver[C].num);
                printf("\nPartido: %s", ver[C].partido);
                break;
            }
            if(C+1 == candidatos)   //caso não tenha candidato correspondente
            ctrl = 2;
        }
        if(ctrl == 2)
        continue;

        printf("\nConfirmar Voto (C-confirmar / D-corrigir): ");
        scanf(" %c", &confirm); fflush(stdin);

        if(confirm == 'C' || confirm == 'c')
        {
        //Soma do voto feito
            for(C=0; C<candidatos; C++)
            {
                if(voto == 0){
                    votosNulos[1]++;
                    break;
                }else if(voto == ver[C].num){
                    ver[C].totalVotos++;
                    break;
                }
            }
        }
    }  
    system("cls");

    for(C=0, total_votos[0]=0; C<candidatos; C++)  //Soma votos p/ Prefeito
    total_votos[0] += pref[C].totalVotos;
    total_votos[0] += votosNulos[0];

    for(C=0, total_votos[1]=0; C<candidatos; C++)  //Soma votos p/ Vereador
    total_votos[1] += ver[C].totalVotos;
    total_votos[1] += votosNulos[1];

    printf("Resultado Prefeito: ");   //Resultado
    for(C=0, ctrl=0; C<candidatos; C++)
    {
    pref[C].percentual_votos = (pref[C].totalVotos * 100) /total_votos[0]; 
        printf("\n\nNome: %s", pref[C].nome);
        printf("\nNumero: %d", pref[C].num);
        printf("\nPartido: %s", pref[C].partido);
        printf("\nTotal de Votos: %d", pref[C].totalVotos);
        printf("\nPercentual de Votos: %.1f %%", pref[C].percentual_votos);

        if(pref[C].totalVotos > ctrl){
            ctrl = pref[C].totalVotos;
            aux = C; 
        }
    }
    percent_nulos[0] = (votosNulos[0] * 100) / total_votos[0];
    printf("\n\nPorcentagem Votos Nulos: %.1f %%", percent_nulos[0]);
    if(ctrl != 0)
    printf("\n\nCandidato Vencedor: %s\n", pref[aux].nome);
    else
    printf("\n\nCandidato Vencedor: n/a\n");


    printf("\n\nResultado Vereador: ");   //Resultado Vereador
    for(C=0, ctrl=0; C<candidatos; C++)
    {
    ver[C].percentual_votos = (ver[C].totalVotos * 100) /total_votos[1]; 
        printf("\n\nNome: %s", ver[C].nome);
        printf("\nNumero: %d", ver[C].num);
        printf("\nPartido: %s", ver[C].partido);
        printf("\nTotal de Votos: %d", ver[C].totalVotos);
        printf("\nPercentual de Votos: %.1f %%", ver[C].percentual_votos);

        //Contagem de maior número de votos
        if(ver[C].totalVotos > ctrl){ 
            ctrl = ver[C].totalVotos;
            aux = C; 
        }
    }
    percent_nulos[1] = (votosNulos[1] * 100) / total_votos[1];
    printf("\n\nPorcentagem Votos Nulos: %.1f %%", percent_nulos[1]);
    if(ctrl != 0)
    printf("\n\nCandidato Vencedor: %s", ver[aux].nome);
    else
    printf("\n\nCandidato Vencedor: n/a\n");
}

    printf("\n\n\nVotacao Finalizada!\n\n");

system("pause");
}
