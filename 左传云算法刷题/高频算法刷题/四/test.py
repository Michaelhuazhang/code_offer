# -*- encoding:utf-8 -*-

class Solution:
	def compare(self, array):
		if not array or len(array) == 0:
			return 0
		temp = [array[0]]
		for x in range(len(array)-1):
			if array[x] < array[x+1]:
				temp.append(array[x+1])
		return temp

	def pingan(self, array):
		times = 1
		temp = self.compare(array)
		while len(temp) != 1:
			times += 1
			a = self.compare(temp)
			if a == s:
				times -= 1
				break
			else:
				b = self.compare(a)
				temp = b
				if a == b:
					times-= 1
					break
				else:
					times += 1
		return times

while 1:
	a = []
	s1 = raw_input()
	s2 = raw_input()
	if s2!= "":
		for x in s2.split():
			a.append(int(x))
			print(Solution().pingan(a))
	else:
		break



import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
 
 
		Scanner inpu = new Scanner(System.in);
		int n=in.nextInt();
		List<Integer> listarray=new ArrayList<Integer>();
		for(int i=0;i<n;i++)
		{
			listarray.add(inpu.nextInt());
		}
		
		int count=0;
		while(listarray.size()>1)
		{
			for(int i=listarray.size()-1;i>=1;i--)
			{
				if(listarray.get(i)<listarray.get(i-1))
				{
					listarray.remove(i);
				}
			}
			if(listarray.size()==n)break;
			else
			{
				n=listarray.size();
				count++;
			}
		}
		System.out.println(count);
 
	}
 
}
 



import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int i = 0; i < T; i++){
			int n = sc.nextInt();
			int X = sc.nextInt();
			int[] record = new int[n];
			for(int j = 0; j < n; j++){
				record[j] = sc.nextInt();
			}
			System.out.println(changeNum(record,n,X));
		}
	}
	//修改成绩的次数
	private static int changeNum(int[] record, int n, int x) {
		int count = 0;
		while(judgeCj(record,n)<x){
			count++;
			int index = minIndex(record);
			record[index] = 100;
		}
		return count;
	}
	//找出数组中最小数字的下标
	private static int minIndex(int[] record) {
		int index = 0;
		for(int i = 0; i < record.length; i++){
			if(record[index] > record[i])
				index = i;
		}
		return index;
	}
	//返回平均分
	private static int judgeCj(int[] record, int n) {
		int result = 0;
		for(int i = 0; i < n; i++){
			result += record[i];
		}
		return result / n;
	}
}
