#include<iostream>
using namespace std;
class Heap
{
	int n;
	int*minheap,*maxheap;
	public:
		void get();
		void displayMin(){cout<<"Minimum marks are:"<<maxheap[0]<<endl;}
		void displayMax(){cout<<"maximum marks are:"<<minheap[0]<<endl;}
		void upAdjust(bool,int);		
};
void Heap::get()
{
	cout<<"enter number of students."<<endl;
	cin>>n;
	int k;
	minheap=new int[n];
	maxheap=new int[n];
	cout<<"enter marks of students."<<endl;
	for(int i=0;i<n;i++)
	{
		cin>>k;
		minheap[i]=k;
		upAdjust(0,i);
		maxheap[i]=k;
		upAdjust(1,i);
	}
}
void Heap::upAdjust(bool m,int l)
{
	int s;
	if(!m)
	{
		while(minheap[(l-1)/2]<minheap[l])
		{
			s=minheap[l];
			minheap[l]=minheap[(l-1)/2];
			minheap[(l-1)/2]=s;
			l=(l-1)/2;
			if(l==-1)
			        break;
		}
	}
	else
	{
		while(maxheap[(l-1)/2]>maxheap[l])
		{
			s=maxheap[l];
			maxheap[l]=maxheap[(l-1)/2];
			maxheap[(l-1)/2]=s;
			l=(l-1)/2;
			if(l==-1)
			       break;
		}
	}
}
main()
{
	Heap H;
	H.get();
	H.displayMax();
	H.displayMin();
	return(0);
}