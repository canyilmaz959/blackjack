#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
int main(){
	srand(time(NULL));
	int pc;
	char secim, tekrar = 'e';
	while (tekrar == 'E' || tekrar == 'e'){
		pc = rand() % 6 + 1;
	    for (int i=1; i<7; i++ ){
	    	printf(" %d. kovan lutfen bir secim yapin\n[C = cek] - [B = birak]\ntetigi: C - B\n=>", i);
		    scanf(" %c", &secim);
		    getchar();
		
		    if (secim == 'C' || secim == 'c'){
			   printf("atesleniyor...\n");
			   Sleep(3000);
			
			   if (i == pc){
				  printf("silah patladi oldun!!!\n");
				  break;
			   }else{
				  printf("silah patlamadi devam\n");}
			
			
		    }else if (secim == 'B' || secim == 'b'){
			    printf("silah birakiliyor...\nmermi %d. kovandaydi\n", pc);
			    break;
				
		   }else{
			    printf("lutfen gecerli bir secim yapiniz!\n");
			    break;}
		   }
		   printf("basa sonmek ister misiniz: (E/H)\n");
		   scanf(" %c", &tekrar);
		   getchar();
		   if (tekrar == 'H' || tekrar == 'h'){
		   	printf("cikiliyor...");
		   	Sleep(2000);
		   }
		   
	}
	
			
		return 0;
		}
	
	
