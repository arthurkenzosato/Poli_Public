#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>
#define  TAMANHO_MAX_NOME_ELEMENTO 15
#define  NUMERO_MAX_SUBMAQUINAS 10
typedef char tipo_elemento_matriz_trasicao[TAMANHO_MAX_NOME_ELEMENTO];

typedef struct _No {
 char info[TAMANHO_MAX_NOME_ELEMENTO];
 struct _No *prox;
} No;


typedef struct _No1 {
 char info;
 struct _No1 *prox;
} No1;

typedef struct _Pilha{
int topo;
No *elementos;
}Pilha;

typedef struct _Pilha1{
int topo;
No1 *elementos;
}Pilha1;

No* livre ;
No1* livre1 ;

void inicializaListaLivre() {
livre = NULL;
}
void inicializaListaLivre1() {
livre1 = NULL;
}
void extraiNo(No **p){
if (livre == NULL) {
*p = (No *) malloc(sizeof(No));

}
else {
*p = livre;
livre = livre->prox;
}
}

void extraiNo1(No1 **p){
if (livre1 == NULL) {
*p = (No1 *) malloc(sizeof(No1));

}
else {
*p = livre1;
livre1 = livre1->prox;
}
}
void devolveNo(No *p) {
p->prox = livre;
livre = p;
}
void devolveNo1(No1 *p) {
p->prox = livre1;
livre1 = p;
}
/* Procedimento para inserir um elemento x na pilha L */
void  empilha(char x[TAMANHO_MAX_NOME_ELEMENTO], Pilha *L){
 No *p;

extraiNo(&p);
strcpy(p->info, x);
//p->info = x;
if ((L)->topo==-1) { /* Pilha vazia */
p->prox = p;
(L)->elementos = p;
}
else {
//p->prox = (L)->elementos->prox;
//(L)->elementos->prox = p;
p->prox = (L)->elementos;
(L)->elementos=p;
}
(L)->topo++;
 }

/* Procedimento para inserir um elemento x na pilha L */
void  empilha1(char x, Pilha1 *L){
 No1 *p;

extraiNo1(&p);
p->info= x;
//p->info = x;
if ((L)->topo==-1) { /* Pilha vazia */
p->prox = p;
(L)->elementos = p;
}
else {
p->prox = (L)->elementos->prox;
(L)->elementos->prox = p;
}
(L)->topo++;
 }
 /* Procedimento para remover um elemento (vetor) da pilha L */
void desempilha(char *x[TAMANHO_MAX_NOME_ELEMENTO], Pilha *L) {
 No *p; /* Aponta para o elemento que vai ser */
/* removido. */

p = (L)->elementos;
strcpy( x , &(L)->elementos->info);


if (L->topo==0){ /* Lista com apenas um no */
L->topo=-1;
L = NULL;
}
else{
(L)->elementos = p->prox;
devolveNo(p);
L->topo--;
}
    //(L)->elementos = (L)->elementos->prox;

}
/* Procedimento para remover um elemento (caractere) da pilha L */
void desempilha1(char *x, Pilha1 *L) {
 No1 *p; /* Aponta para o elemento que vai ser */
/* removido. */

p = (L)->elementos;
*x = p->info;

if (L->topo==0){ /* Lista com apenas um no */
L->topo=-1;
L = NULL;
}
else
(L)->elementos = p->prox;
devolveNo1(p);
}


//estrutura basica de um automato simples
typedef struct  {
tipo_elemento_matriz_trasicao    matriz_transicao[300][3];
int quantidade_de_transicoes;
char estado_inicial[TAMANHO_MAX_NOME_ELEMENTO];
} sub_maquina ;

//estrutura do automato de pilha estruturada
typedef struct  {
int numero_submaquinas;
sub_maquina     sub_maquina[NUMERO_MAX_SUBMAQUINAS];
tipo_elemento_matriz_trasicao nome_submaq[NUMERO_MAX_SUBMAQUINAS];
char submaquina_primaria[TAMANHO_MAX_NOME_ELEMENTO];
char submaquina_atual[TAMANHO_MAX_NOME_ELEMENTO];
char estado_atual[TAMANHO_MAX_NOME_ELEMENTO];

} automato ;

// funçao que checa se existe a transicao na matriz e realiza transicao caso tenha
char    busca_e_realiza_transicao( sub_maquina    *M   , char *estado_atual_lexico[TAMANHO_MAX_NOME_ELEMENTO] ,   char caractere_lido){
    int k=0;

    while(  k<(*M).quantidade_de_transicoes ){
        if( strncmp( &((*M).matriz_transicao[k][0]), estado_atual_lexico, sizeof(tipo_elemento_matriz_trasicao) )==0   &&  strncmp( &((*M).matriz_transicao[k][1]), &caractere_lido , 1 )==0 ){//checa se tem a transicao na matriz

            strncpy ( estado_atual_lexico, (*M).matriz_transicao[k][2], sizeof(tipo_elemento_matriz_trasicao) ); //se tem trasicao, realiza
            return 'T';
        }
    k++;
    }
    return 'F';
}
// funçao que checa se existe a transicao na matriz e realiza transicao caso tenha
char    busca_e_realiza_transicao_lendo_vetor( sub_maquina    *M   , char *estado_atual[TAMANHO_MAX_NOME_ELEMENTO] ,   char caractere_lido[TAMANHO_MAX_NOME_ELEMENTO]){
    int k=0;

    while(  k<(*M).quantidade_de_transicoes ){
        if( strncmp( &((*M).matriz_transicao[k][0]), estado_atual, sizeof(tipo_elemento_matriz_trasicao) )==0   &&  strncmp( ((*M).matriz_transicao[k][1]), caractere_lido ,sizeof(tipo_elemento_matriz_trasicao ))==0 ){//checa se tem a transicao na matriz

            strncpy ( estado_atual, (*M).matriz_transicao[k][2], sizeof(tipo_elemento_matriz_trasicao) ); //se tem trasicao, realiza
            return 'T';
        }
    k++;
    }
    return 'F';
}





// funcao que le matriz do arquivo e constroi matriz no programa
void    le_matriz(sub_maquina    *M ,    FILE    *arq1  ){
        int i=0,j=0;
        char x[TAMANHO_MAX_NOME_ELEMENTO];

        (*M).quantidade_de_transicoes=0;
        fscanf(arq1, "%s", &x);

        while(x[0]!='!'){//enquanto for diferente de ! le arquivo

            if(x[0]=='*'){
            //strncpy ( estado_final, x, sizeof(estado_final) );
            }
            strncpy ( (*M).matriz_transicao[i][j], x, sizeof(tipo_elemento_matriz_trasicao) );

            j++;
            if(j==3){
                j=0;
                i++;
                (*M).quantidade_de_transicoes++;
            }
        fscanf(arq1, "%s", &x);
        }
    }
// funcao que le arquivo contendo automato e monta a estrutura
void    le_automato(automato  *A ,    FILE    *arq3  ){

    char x[TAMANHO_MAX_NOME_ELEMENTO];
    int i=0,j=0;
    int tamanho;


        fscanf(arq3, "%s", &x);


        (*A).numero_submaquinas=0;          // inicio tem 0 submaquinas
        strncpy ( (*A).submaquina_primaria , x, sizeof(tipo_elemento_matriz_trasicao) ); // le submaquina primaria do arquivo
        strncpy ( (*A).submaquina_atual , x, sizeof(tipo_elemento_matriz_trasicao) );    // submaquina primaria é a que começa


        while(x[0]!=';'){

         strncpy ( (*A).nome_submaq[i] , x, sizeof(tipo_elemento_matriz_trasicao) );    //copia nome das submaquinas
         i++;
         (*A).numero_submaquinas++;
         fscanf(arq3, "%s", &x);
         }

       tamanho=(*A).numero_submaquinas;
       fscanf(arq3, "%s", &x);
       strncpy (&(*A).estado_atual,  x,  sizeof(tipo_elemento_matriz_trasicao) );
       while(tamanho!=0){

            strncpy (&(*A).sub_maquina[j].estado_inicial,  x,  sizeof(tipo_elemento_matriz_trasicao) ); // le estado inicial de cada submaquina
            le_matriz(&(*A).sub_maquina[j] ,   arq3  ); //constroi a matriz das submaquinas
            fscanf(arq3, "%s", &x);
            j++;



         tamanho--;
}
}

// funcao que confere se a presente transicao é para submaquina
char check_se_eh_transicao_para_submaquina (sub_maquina *M, automato *A, char *nome_submaquina_chamada[TAMANHO_MAX_NOME_ELEMENTO],char *estado_retorno){
int i,j;
     for(    i=0 ;  i<(*M).quantidade_de_transicoes   ; i++    ){ //varre matriz transicao
            for(    j=0;     j<(*A).numero_submaquinas;  j++   ){ //varre nome das submaquinas
                    if( strcmp((*A).estado_atual, (*M).matriz_transicao[i][0] )==0 && strcmp((*A).nome_submaq[j] , (*M).matriz_transicao[i][1] )==0){      //procura trancicao na matriz e checa se termo lido é de transicao para submaquina
                        strcpy( nome_submaquina_chamada, (*A).nome_submaq[j] );
                        strcpy( estado_retorno, (*M).matriz_transicao[i][2] ); //devolve estado de retorno da submaquina
                        return 'T';
                    }
            }
     }

        return 'F';

}
// funçao que checa se existe a transicao na matriz e realiza transicao caso tenha
char    busca_e_realiza_transicao_automato( automato    *A   , char token[TAMANHO_MAX_NOME_ELEMENTO] , Pilha *Pilha_submaquina, Pilha *Pilha_estado,    char cadeia_parcial[TAMANHO_MAX_NOME_ELEMENTO]){

int i=0;
int submaquina=0;
char teve_transicao;
char nome_submaquina_chamada[TAMANHO_MAX_NOME_ELEMENTO];
char nome_submaquina_retorno[TAMANHO_MAX_NOME_ELEMENTO];
char estado_retorno[TAMANHO_MAX_NOME_ELEMENTO];

        for(    i=0 ;   i<(*A).numero_submaquinas  ; i++    ){ // obtem o indice da submaquina
            if(strcmp((*A).submaquina_atual, (*A).nome_submaq[i] )==0)
                submaquina=i;
        }

        //checa se é estado de transicao para submaquina

        if(check_se_eh_transicao_para_submaquina( &(*A).sub_maquina[submaquina]    ,   A,  &nome_submaquina_chamada,    &estado_retorno)=='T'){ //se teve transicao para submaquina

            empilha((*A).submaquina_atual, Pilha_submaquina); //empilha submaquina atual
            empilha(estado_retorno, Pilha_estado); //empilha estado de retorno

            for(    i=0 ;   i<(*A).numero_submaquinas  ; i++    ){ // obtem o indice da nova submaquina
            if(strcmp(nome_submaquina_chamada, (*A).nome_submaq[i] )==0)
                submaquina=i;
        }

            strcpy((*A).estado_atual, (*A).sub_maquina[submaquina].estado_inicial  ); // atualiza estado atual do automato com estado inicial da submaquina chamada
            strcpy((*A).submaquina_atual, nome_submaquina_chamada ); // atualiza submaquina atual no automato

        }


        printf("\n|\t%s\t|\t%s\t|  (%s,%s)\t|\t",  (*A).estado_atual  , (*A).submaquina_atual, cadeia_parcial,token);


            teve_transicao =   busca_e_realiza_transicao_lendo_vetor(  &(*A).sub_maquina[submaquina]    ,   (*A).estado_atual,   token    );

            printf("%s\t",  (*A).estado_atual );

            if((*Pilha_submaquina).topo !=  -1){
            printf("|\t%s\t",   (*Pilha_submaquina).elementos->info);
            }
            if((*Pilha_estado).topo!=-1){
            printf("|\t%s\t\t|",   (*Pilha_estado).elementos->info);
            }
            if((*Pilha_submaquina).topo ==  -1){
            printf("|\tvazio\t");
            }
            if((*Pilha_estado).topo==-1){
            printf("|\tvazio\t\t|");
            }


         while(teve_transicao=='F'){

            desempilha( &nome_submaquina_retorno ,   Pilha_submaquina   );  // desempillha submaquina

            desempilha( &estado_retorno ,   Pilha_estado   );               //desempilha estado de retorno
            for(    i=0 ;   i<(*A).numero_submaquinas  ; i++    ){ // obtem o indice da nova submaquina
            if(strcmp(nome_submaquina_retorno, (*A).nome_submaq[i] )==0)
                submaquina=i;
            }
            strcpy((*A).estado_atual, estado_retorno  ); // atualiza estado atual do automato com estado inicial da submaquina de retorno
            strcpy((*A).submaquina_atual, nome_submaquina_retorno ); // atualiza submaquina atual no automato

            printf("\n|\t%s\t|\t%s\t|  (%s,%s)\t|\t",  (*A).estado_atual  , (*A).submaquina_atual, cadeia_parcial,token);


            teve_transicao =   busca_e_realiza_transicao_lendo_vetor(  &(*A).sub_maquina[submaquina]    ,   (*A).estado_atual,   token    );

            printf("%s\t",  (*A).estado_atual );

            if((*Pilha_submaquina).topo !=  -1){
            printf("|\t%s\t",   (*Pilha_submaquina).elementos->info);
            }
            if((*Pilha_estado).topo!=-1){
            printf("|\t%s\t\t|",   (*Pilha_estado).elementos->info);
            }

            if((*Pilha_submaquina).topo ==  -1){
            printf("|\tvazio\t");
            }
            if((*Pilha_estado).topo==-1){
            printf("|\tvazio\t\t|");
            }

         }


}









int main()
{   FILE    *arq1,*arq2,*arq3;
    char    nomeEntrada[20],nomeCadeiaEntrada[20],nomeAutomato[20];

    char    existe_transicao;
    char    estado_atual_lexico[TAMANHO_MAX_NOME_ELEMENTO];
    char    caractere_lido;
    char    cadeia_parcial[TAMANHO_MAX_NOME_ELEMENTO];

    char    token[TAMANHO_MAX_NOME_ELEMENTO];
    Pilha   Pilha_maquinas,Pilha_estado;
    Pilha1  P;
    sub_maquina     Ana_lexico;
    automato        Automato;
    int     termo_cadeia_parcial=0;
    int     i;

    printf("Digite o nome do arquivo de entrada(lexico): ");
    scanf("%s",nomeEntrada);
    printf("Digite o nome do arquivo que contem a cadeia de entrada: ");
    scanf("%s",nomeCadeiaEntrada);
     printf("Digite o nome do arquivo que contem o automato de pilha: ");
    scanf("%s",nomeAutomato);

    arq1= fopen(nomeEntrada,"r");
    arq2= fopen(nomeCadeiaEntrada,"r");
    arq3= fopen(nomeAutomato,"r");

    Ana_lexico.quantidade_de_transicoes=0; //inicializa quantidade de transicoes do analisador lexico
    P.topo=-1; //pilha vazia
    Pilha_maquinas.topo=-1;// pilha maquinas vazia
    Pilha_estado.topo=-1;//pilha estado vazia

    fscanf(arq1, "%s", &Ana_lexico.estado_inicial);
    strcpy(estado_atual_lexico, Ana_lexico.estado_inicial);              // estado_atual_lexico deve ser inicializado

    le_matriz(&Ana_lexico ,    arq1);               //constroi a matriz do analisador lexico partindo do arquivo q contem as transiçoes
    le_automato(&Automato ,    arq3);               //constroi automato partindo do arquivo de texto





     printf("\n|    estado     |   submaquina  |     token     |    novo estado | Pilha_submaq   | Pilha_estado_retorno |");
     printf("\n|--------------------------------------------------------------------------------------------------------|");
    fscanf(arq2, "%c", &caractere_lido);
    while(caractere_lido==' '||caractere_lido=='\n'){                   // se ler espaço ou enter ignora
        fscanf(arq2, "%c", &caractere_lido);
    }


    while(caractere_lido!='&'){     //arquivo com cadeia de entrada deve terminar com &

            //le caracteres de entrada, se termo


        if(P.topo==-1){              //se pilha vazia
            existe_transicao= busca_e_realiza_transicao( &Ana_lexico   , &estado_atual_lexico ,  caractere_lido);

                if(existe_transicao=='F'){
                    empilha1(caractere_lido,&P);
                    strcpy (token , estado_atual_lexico);
                    strcpy (estado_atual_lexico , Ana_lexico.estado_inicial);
                    for(i=0;i<14;i++){
                        token[i]=token[i+1];
                    }


                    cadeia_parcial[termo_cadeia_parcial]='\0'; //termina string


                  //chama analisador sintatico
                    busca_e_realiza_transicao_automato( &Automato   ,token , &Pilha_maquinas,  &Pilha_estado, cadeia_parcial);
                    termo_cadeia_parcial=0;
                }
               if(existe_transicao=='T'){
                cadeia_parcial[termo_cadeia_parcial]=caractere_lido;
                termo_cadeia_parcial++;
                fscanf(arq2, "%c", &caractere_lido);
                    while(caractere_lido==' '||caractere_lido=='\n'){// se ler espaço ou enter ignora
                        fscanf(arq2, "%c", &caractere_lido);
                    }

               }



       }
        if(P.topo!=-1){
            termo_cadeia_parcial=0;
            desempilha1(&caractere_lido, &P);
            cadeia_parcial[termo_cadeia_parcial]=caractere_lido;
            existe_transicao= busca_e_realiza_transicao( &Ana_lexico   , &estado_atual_lexico ,  caractere_lido);
                if(existe_transicao=='F'){
                    empilha1(caractere_lido,&P);
                    strcpy (estado_atual_lexico , Ana_lexico.estado_inicial);
                    strcpy (token , estado_atual_lexico);
                    for(i=0;i<14;i++){
                        token[i]=token[i+1];
                    }

                    cadeia_parcial[termo_cadeia_parcial]='\0'; //termina string

                    //chama analisador sintatico

                  busca_e_realiza_transicao_automato( &Automato   ,token , &Pilha_maquinas,  &Pilha_estado, cadeia_parcial);
                    termo_cadeia_parcial=0;
                }
                if(existe_transicao=='T'){
                    cadeia_parcial[termo_cadeia_parcial]=caractere_lido;
                    termo_cadeia_parcial++;
                    fscanf(arq2, "%c", &caractere_lido);
                        while(caractere_lido==' '||caractere_lido=='\n'){// se ler espaço ou enter ignora
                            fscanf(arq2, "%c", &caractere_lido);
                        }

               }
        }

    if(caractere_lido=='&'){
        strcpy (token , estado_atual_lexico);
        for(i=0;i<14;i++){
            token[i]=token[i+1];
        }

        cadeia_parcial[termo_cadeia_parcial]='\0'; //termina string

        //chama analisador sintatico

         busca_e_realiza_transicao_automato( &Automato   ,token , &Pilha_maquinas,  &Pilha_estado, cadeia_parcial);
    }



    }


 fclose(arq1);
 fclose(arq2);
 fclose(arq3);
 printf("\n");
 system("pause");

    return 0;
}
