static final int NUMERO_CUBOS = 20;
static final int NUMERO_PISTAS = 6;
static final int LARGURA_DA_TELA = 1000;
static final int ALTURA_DA_TELA = 700;
Cubo[] cubos = new Cubo[NUMERO_PISTAS];
Personagem personagem = new Personagem();
float SpawnDaPista[] = new float[NUMERO_PISTAS];
float theta = 0;
float alpha = 255;
float xPersonagem = LARGURA_DA_TELA/(NUMERO_PISTAS+1) * int(random(1,NUMERO_PISTAS+1));
float yPersonagem = ALTURA_DA_TELA - 50;
int pontos;
boolean pontua = false;
int dificuldade = 1;
Cubo pontuaCubo = new Cubo(0,3);
int framesDaPontuacao = 0;
boolean iniciaPontuacao = false;



//Botoes
float posBotaoX;
float posBotaoY;
float BotaoWidth;
float BotaoHeight;
float posBotao2X;
float posBotao2Y;

//Controle
int modoJogo;
int botao;

//Imagens
PImage Inicial;
PImage botaoJogar;
PImage botaoInstru;
PImage Instrucao;
PImage tituloInstrucao;
PImage tituloPontuacao;





void gerarBotao1(){
  //Jogar
  //fill(255);
  //rect(posBotaoX,posBotaoY,BotaoWidth,BotaoHeight);
   image(botaoJogar,posBotaoX,posBotaoY,BotaoWidth,BotaoHeight);
   botao = 1; 
}

void gerarBotao2(){
  //Instrucao
  //fill(0,255,0);
  //rect(posBotao2X,posBotao2Y,BotaoWidth,BotaoHeight);
  image(botaoInstru,posBotao2X,posBotao2Y,BotaoWidth,BotaoHeight);
  botao = 1;
}

void gerarBotao3(){


 image(botaoJogar,375,600,BotaoWidth,BotaoHeight);
 botao = 1;
}

void telaInicial(){
  image(Inicial, 150, 60, 715, 112);
}


void telaInstrucao(){
 image(tituloInstrucao,350,50,250,100); 
 image(Instrucao, 100, 200, 800 ,400); 
  
}


void setup(){
 frameRate(60);
  size(LARGURA_DA_TELA,ALTURA_DA_TELA,P3D);
  ortho(0, width, 0, height);
  camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0);
  
  //Instanciando Pistas e Cubos
  float largura = 0;
  for(int i= 0; i < NUMERO_PISTAS; i++) {
    largura += LARGURA_DA_TELA/(NUMERO_PISTAS+1);
    SpawnDaPista[i] = largura;
  }
  for(int i = 0; i < (NUMERO_PISTAS); i++) {
    cubos[i] = new Cubo (SpawnDaPista[i], 3);
  }
  pontuaCubo.r = 255;
  pontuaCubo.g = 255;
  pontuaCubo.b = 255;
  pontuaCubo.cor = color(255, 255, 255, alpha);
  pontuaCubo.yvelocidade = -1;
  personagem.vidas=3;
  
  Inicial= loadImage("blacktowhite.png");
  botaoJogar = loadImage("botao_jogar.png");
  botaoInstru = loadImage("botao_instrucoes.png");
  Instrucao = loadImage("instrucoes_02.png");
  tituloInstrucao = loadImage("instrucoes_01.png");
  tituloPontuacao = loadImage("pontuacao.png");
  

  BotaoWidth = LARGURA_DA_TELA/6;
  posBotaoX = (LARGURA_DA_TELA/2)-(BotaoWidth/2);
  posBotaoY = ALTURA_DA_TELA*(0.5);
  BotaoHeight = ALTURA_DA_TELA/10;
  
  posBotao2X=posBotaoX;
  posBotao2Y=ALTURA_DA_TELA*(0.75);
  modoJogo = 0;
  botao=0;
}





void draw(){
  switch(modoJogo){
    case 0:
    background(0);
    telaInicial();
    gerarBotao1();
    gerarBotao2();
   
    break;
    
    
    
    case 1:
///////  Instrucoes
    background(0);
    telaInstrucao();
    gerarBotao3();
    
    break;
    
    
    case 2:
// Definições do Background
  lights();
  background(0);
  //telaInicial();
  
  
  // Definição da rotação do objeto
  theta = theta+0.05;
  if(personagem.vidas==0){
    modoJogo = 3;
    personagem.reiniciaPosicao();
    personagem.reiniciaCor();
  }
    
  // Definição da pontuação
  pushMatrix();
  stroke(0);
  rectMode(CORNER);
  fill(100, 150, 100);
  rect(0, 0, LARGURA_DA_TELA/8, ALTURA_DA_TELA/14);
  fill(255, 255, 255);
  text (" PONTOS : ", 10, 20, 0);
  text (pontos, 90, 20, 0);
  text (" VIDAS : ", 10, 40, 0);
  //text (personagem.vidas, 100, 40, 0);20 100
  popMatrix();
  
  if (personagem.vidas > 0) {
    pushMatrix(); 
    translate(70, 35, 00);
    rotateY(theta);
    stroke(0);
    fill(255,255,255);
    box(10);
    popMatrix();  
  }
  
  if (personagem.vidas > 1) {
    pushMatrix(); 
    translate(90, 35, 00);
    rotateY(theta);
    stroke(0);
    fill(255,255,255);
    box(10);
    popMatrix();  
  }
  
  if (personagem.vidas > 2) {
    pushMatrix(); 
    translate(110, 35, 00);
    rotateY(theta);
    stroke(0);
    fill(255,255,255);
    box(10);
    popMatrix();  
  }
  
  //Cubo, rotacionar antes de desenhar o objeto
  
  // Percorre todas as pistas
  for(int i = 0; i < NUMERO_PISTAS; i++) {
    // Refresh nos cubos ativos
    if(cubos[i].alive){
      pushMatrix();
      translate(cubos[i].xpos, cubos[i].ypos, 00);
      rotateX(theta/2);
      rotateZ(theta);
      cubos[i].display();
      cubos[i].avanca();
      popMatrix();
    }
    
    // Definição das pistas por uma reta
    pushMatrix();
    stroke(200);
//    line(SpawnDaPista[i],0,SpawnDaPista[i],700);
    popMatrix();
  }
  
  // Timer para startar cubos
  switch (dificuldade) {
    // Dificuldade Nível 1
    case 1:
      if((frameCount % 100) == 0) {
        int randomPista = int(random(0,NUMERO_PISTAS));
        cubos[randomPista].alive = true;
        pushMatrix();
        translate(cubos[randomPista].xpos, cubos[randomPista].ypos, 00);
        rotateX(theta/2);
        rotateZ(theta);
        cubos[randomPista].display();
        cubos[randomPista].avanca();
        popMatrix();
      }
      break;
      
    // Dificuldade Nível 2
    case 2:
      if((frameCount % 40) == 0) {
        int randomPista = int(random(0,NUMERO_PISTAS));
        cubos[randomPista].alive = true;
        pushMatrix();
        translate(cubos[randomPista].xpos, cubos[randomPista].ypos, 00);
        rotateX(theta/2);
        rotateZ(theta);
        cubos[randomPista].yvelocidade = 4;
        cubos[randomPista].display();
        cubos[randomPista].avanca();
        popMatrix();
      }
      break;       
      
    // Dificuldade Nível 3
    case 3:
      if((frameCount % 30) == 0) {
        int randomPista = int(random(0,NUMERO_PISTAS));
        cubos[randomPista].alive = true;
        pushMatrix();
        translate(cubos[randomPista].xpos, cubos[randomPista].ypos, 00);
        rotateX(theta/2);
        rotateZ(theta);
        cubos[randomPista].yvelocidade = 5;
        cubos[randomPista].display();
        cubos[randomPista].avanca();
        popMatrix();
      }
      break;
    
    // Dificuldade Nível 4
    case 4:
      if((frameCount % 18) == 0) {
        int randomPista = int(random(0,NUMERO_PISTAS));
        cubos[randomPista].alive = true;
        pushMatrix();
        translate(cubos[randomPista].xpos, cubos[randomPista].ypos, 00);
        rotateX(theta/2);
        rotateZ(theta);
        if ( cubos[randomPista].yvelocidade < 11){
          cubos[randomPista].yvelocidade += 1;
        }
        cubos[randomPista].display();
        cubos[randomPista].avanca();
        popMatrix();
      }
    
    default:
        ;
  }
  if (pontos == 2) {
    dificuldade = 2;
  }
  if (pontos == 5) {
    dificuldade = 3;
  }
  if (pontos == 10) {
    dificuldade = 4;
  }
  // Refresh no personagem
  pushMatrix();
  translate(personagem.xpos, personagem.ypos, 00);
  rotateY(theta);
  personagem.atualizaPosicao();
  personagem.display();
  popMatrix();
  
  // Hit Test
  for (int i = 0; i < NUMERO_PISTAS; i++) {
    // Hit!!
    if (cubos[i].hitTest(xPersonagem, yPersonagem)) {
      if ((personagem.r == 0) && (personagem.g == 0) && (personagem.b == 0) && (cubos[i].alive == true)) {
        personagem.r += cubos[i].r;
        personagem.g += cubos[i].g;
        personagem.b += cubos[i].b;
        personagem.atualizaCor();
        pontua = false;
        cubos[i].alive = false;
        cubos[i].ypos = 0;
      }
      else {
        // Cor do personagem igual a Cor do cubo
        if (((personagem.r == 255 && cubos[i].r == 255) || (personagem.g == 255 && cubos[i].g == 255) || (personagem.b == 255 && cubos[i].b == 255)) && (cubos[i].alive == true)) {
          background(255);
          personagem.reiniciaCor();
          personagem.atualizaCor();
          personagem.vidas--;
        }
        // Cor do personagem diferente da Cor do cubo
        else {
          personagem.r += cubos[i].r;
          personagem.g += cubos[i].g;
          personagem.b += cubos[i].b;
          personagem.atualizaCor();
        }
        cubos[i].alive = false;
        cubos[i].ypos = 0;
      }
    }
  }
  
  //Personagem atingiu a meta de chegar na cor Branca!! Ponto!!
  if ((personagem.r == 255) && (personagem.g == 255) && (personagem.b == 255) && (pontua == false)) {
    pontos += 1;
    personagem.reiniciaCor();
    personagem.atualizaCor();
    pontua = true;
    pontuaCubo.xpos = personagem.xpos;
    pontuaCubo.ypos = personagem.ypos;
    iniciaPontuacao = true;
  }
  
  if (iniciaPontuacao == true) {
    iniciaFade();
    framesDaPontuacao++;
    if (framesDaPontuacao > 30) {
      framesDaPontuacao = 0;
      iniciaPontuacao = false;
      alpha = 255;
      pontuaCubo.cor = color(255, 255, 255, alpha);  
    }
  }
    break;
    
    case 3:
    //Tela da morte
 
   background(0);
    pushMatrix();
    stroke(0);
    //rectMode(CORNER);
    fill(255, 255, 255);
    textSize(40);
    text (" MINHA VÓ JOGA MELHOR QUE VOCÊ!!! ", 100, 100, 0);
    text (" PONTOS : ", 100, 400, 0);
    text (pontos, 600, 400, 0);
    popMatrix();
    gerarBotao1();
    gerarBotao2();
    textSize(12);
    

    break;
      
    
  
  
  
  }
 
 
}




void mouseReleased(){
    
  
   
  
  
   if(modoJogo==0 && botao==1 && mouseX>posBotaoX && mouseX<(posBotaoX+BotaoWidth) && mouseY>posBotaoY && mouseY<(posBotaoY+BotaoWidth)){
    background(255);
    modoJogo=2; //Jogar
    botao=0;
   }
   if(modoJogo==0 && botao==1 && mouseX>posBotao2X && mouseX<(posBotao2X+BotaoWidth) && mouseY>posBotao2Y && mouseY<(posBotao2Y+BotaoWidth)){
     background(255);
     modoJogo=1; //Instrucao
     botao=0;
   } 
   
     
   if(modoJogo==1 && botao==1 && mouseX>375 && mouseX<(375+BotaoWidth) && mouseY>600 && mouseY<(600+BotaoWidth)){
    background(255);
    modoJogo=2; //Jogar
    botao=0;
    
    
   }  
     
   
   if(modoJogo==3 && botao==1 && mouseX>posBotao2X && mouseX<(posBotao2X+BotaoWidth) && mouseY>posBotao2Y && mouseY<(posBotao2Y+BotaoWidth)){
     background(255);
     modoJogo=1; //Instrucao
     botao=0;
   } 
    
     
     
    if(modoJogo==3 && botao==1 && mouseX>posBotaoX && mouseX<(posBotaoX+BotaoWidth) && mouseY>posBotaoY && mouseY<(posBotaoY+BotaoWidth)){
    // background(255);
     modoJogo=2; //Jogar
     personagem.vidas=3;
     botao=0;
   } 
   
   
    
}




void iniciaFade() {
  pushMatrix();
  translate(pontuaCubo.xpos, pontuaCubo.ypos, 00);
  rotateY(theta);
  pontuaCubo.avanca();
  pontuaCubo.display();
  popMatrix();
  alpha -= (255/30);
  pontuaCubo.cor = color(255, 255, 255, alpha);
}


////////////////////////////////////////////////////////////

class Personagem {
  color cor;
  float xpos, ypos;  
  int r, g, b = 0;
  int vidas;
  
  //Construtor do personagem
  Personagem() {
     r = 0;
     g = 0;
     b = 0;
     cor = color(r,g,b);
     vidas = 3;
  }
  
  void atualizaPosicao() {
    xpos = xPersonagem;
    ypos = yPersonagem;
  }  
  
  void atualizaCor() {
    cor= color(r, g, b);
  }
  
  void display() {
    stroke(255);
    fill(cor);
    box(50);
  }
  
  void reiniciaCor() {
    r = 0;
    g = 0;
    b = 0;
  }
  
  void reiniciaPosicao() {
    xPersonagem = LARGURA_DA_TELA/(NUMERO_PISTAS+1) * int(random(1,NUMERO_PISTAS+1));
    yPersonagem = ALTURA_DA_TELA - 50;
  }
}



////////////////////////////////////////////////////
class Cubo {
  color cor;
  float xpos, ypos, yvelocidade;
  int r, g, b = 0;
  boolean alive = false;
  
  // Construtor do Cubo
  Cubo(float tempXpos, float tempYvelocidade) {
    
    int escolhe_cor = int(random(1,4));
    
    switch (escolhe_cor) {
      // cor Vermelho (RED)
      case 1:
        r = 255;
        cor = color(r, 0, 0);
        break;
        
      // cor Verde (GREEN)
      case 2:
        g = 255;
        cor = color(0, g, 0);
        break;
        
      // cor Azul (BLUE)
      case 3:
        b = 255;
        cor = color(0, 0, b);
        break;
      default:
        cor = color(100, 100, 100);
    }
    
    xpos = tempXpos;
    ypos = -200;
    yvelocidade = tempYvelocidade;
    alive = false;
  }
  
  // Verifica se houve hit
  boolean hitTest (float mx, float my) {
    if (dist (xpos, ypos, mx, my) < 50) {
      return true;
    } else return false;
  }
  
  void display() {
    stroke(0);
    fill(cor);
    box(50);
  }
  
  void avanca() {
    ypos = ypos + yvelocidade;
    if (ypos > ALTURA_DA_TELA) {
      ypos = 0;
      r = 0;
      g = 0;
      b = 0;
      int escolhe_cor = int(random(1,4));
      
      switch (escolhe_cor) {
        // cor Vermelho (RED)
        case 1:
          r = 255;
          cor = color(r, 0, 0);
          break;
          
        // cor Verde (GREEN)
        case 2:
          g = 255;
          cor = color(0, g, 0);
          break;
          
        // cor Azul (BLUE)
        case 3:
          b = 255;
          cor = color(0, 0, b);
          break;
      }
    }
  } 
}

/////////////////////////////////////////////

//Movimentaçao do persanagem
void keyPressed() {
  if (keyCode == UP) {
    if (yPersonagem > 100) {
      yPersonagem -= 70;
    }
  }
  else if (keyCode == DOWN) {
    if (yPersonagem < ALTURA_DA_TELA - 50) {
      yPersonagem += 70;
    }
    
  }
  if (keyCode == RIGHT) {
    if (xPersonagem < (LARGURA_DA_TELA/(NUMERO_PISTAS+1))*(NUMERO_PISTAS)) {
      xPersonagem += LARGURA_DA_TELA/(NUMERO_PISTAS+1);
    }
  }
  else if (keyCode == LEFT) {
    if (xPersonagem > LARGURA_DA_TELA/(NUMERO_PISTAS+1)) {
      xPersonagem -= LARGURA_DA_TELA/(NUMERO_PISTAS+1);
    }
  }
}
