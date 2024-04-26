#include <iostream>
#include <clocale>

using namespace std;

int main() { 
	setlocale(LC_ALL, "Portuguese");
	float t1, t2, t3; 
	string n1, n2, n3; 
	cout<<"Informe o nome do primeiro atleta:";
	cin>>n1;
	cout<<"Informe o tempo do primeiro atleta:";
	cin>>t1;
	cout<<"Informe o nome do segundo atleta:";
	cin>>n2;
	cout<<"Informe o tempo do segundo atleta:";
	cin>>t2;
	cout<<"Informe o nome do terceiro atleta:";
	cin>>n3;
	cout<<"Informe o tempo do terceiro atleta:";
	cin>>t3;			
	
	if (t1 < t2) {
		if (t1 < t3) {
			cout<<n1<<" Campeão"<<endl; 
			if (t2 < t3) { 
				cout<<n2<<" Vice-campeão"<<endl; 
				cout<<n3<<" Terceiro Lugar"<<endl; 
			} else { 
				cout<<n3<<" Vice-campeão"<<endl; 
				cout<<n2<<" Terceiro Lugar"<<endl; 
			}
		} else {
			cout<<n3<<" Campeão"; 
			if (t1 < t2) { 
				cout<<n1<<" Vice-campeão"<<endl; 
				cout<<n2<<" Terceiro Lugar"<<endl; 
			} else { 
				cout<<n2<<" Vice-campeão"<<endl; 
				cout<<n1<<" Terceiro Lugar"<<endl; } 
			} 
	} else { //t2 ganha do t1 
		if (t2 < t3) { 
			cout<<n2<<" Campeão"<<endl; 
			if (t1 < t3) { 
				cout<<n1<<" Vice-campeão"<<endl; 
				cout<<n3<<"Terceiro Lugar"<<endl; 
			} else { 
				cout<<n3<<" Vice-Campeão"<<endl; 
				cout<<n1<<" Terceiro Lugar"<<endl; 
			} 
		} else { 
			cout<<n3 <<" Campeão"<<endl; 
			if (t1 < t2) { 
				cout<<n1<<" Vice-Campeão"<<endl; 
				cout<<n2<<" Terceiro Lugar"<<endl; 
			} else { 
				cout<<n2<<" Vice-Campeão"<<endl; 
				cout<<n1<<" Terceiro Lugar"<<endl; 
			} 
		} 
	} 
	return 0;
}
