#include<time.h>
#include<stdlib.h>
#include<stdio.h>
#include<windows.h>
int main(){
	
	char karar = 'c', cikis = 'E';
	int bilgisayar, kart, kart2b, kart2, oyuncu, kartlar[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	
	srand(time(NULL));
	
	while (cikis == 'e' || cikis == 'E'){
		bilgisayar = rand() % 10;
		printf("kasa: %d\n", kartlar[bilgisayar]);
		Sleep(1000);
		
		oyuncu = rand() % 10 + 1;
		printf("oyuncu: %d\n", oyuncu);
		Sleep(1000);
		
		printf("kart cekiliyor...\n");
		Sleep(3000);
		karar = 'c';
		
		while ( karar == 'c' || karar == 'C'){
			kart = rand() % 10;
			bilgisayar = bilgisayar + kartlar[kart];
			kart2 = rand() % 10;
			oyuncu = oyuncu + kartlar[kart2];			
			
			if (bilgisayar > 21){
				printf("oyuncu kazandi: %d\nkasa : %d\n", oyuncu, bilgisayar);
				break;
			}else if (bilgisayar == 21){
				printf("kasa kazandi: %d\noyuncu : %d\n", bilgisayar, oyuncu);
				break;
			}else if (oyuncu > 21){
				printf("kasa kazandi: %d\noyuncu : %d\n", bilgisayar, oyuncu);
				break;
			}else if (oyuncu == 21){
				printf("oyuncu kazandi: %d\nkasa : %d\n", oyuncu, bilgisayar);
				break;
			}else{
				printf("kasa: %d\noyuncu: %d\ndevam ediliyor...\n", bilgisayar, oyuncu);
				Sleep(2000);}
			
			printf("kart cekmek istiyor musunuz\n[C = cek] - [K = kal]\n=>");
			scanf(" %c", &karar);
			getchar();
			printf("kart cekiliyor...\n");
			Sleep(3000);
			
			if (karar == 'k' || karar == 'K'){
				a:
				printf("kasa kart cekiyor...\nkasa: %d\n", bilgisayar);
				Sleep(2000);
				kart2b = rand() % 10 + 1;
				bilgisayar = bilgisayar + kart2b;
				
				if (bilgisayar > 21){
				    printf("oyuncu kazandi: %d\nkasa: %d\n", oyuncu, bilgisayar);
					break;
				}else if (bilgisayar < oyuncu){
					printf("kasa: %d\n", bilgisayar);
					goto a;
				}else if (bilgisayar == oyuncu){
				    printf("oyun berabere!!\nkasa: %d\noyuncu: %d\n", bilgisayar, oyuncu);
				    break;
				}else{
					printf("kasa kazandi: %d\noyuncu: %d\n", bilgisayar, oyuncu);
					break;}	
			}
			}
			
		printf("\nyeniden oynamak ister misiniz: (E/H)");
		scanf(" %c", &cikis);
		getchar();
		
		if (cikis == 'h' || cikis == 'H'){
			printf("cikiliyor...");
			Sleep(3000);
		}
		}
		
		return 0;
	}
