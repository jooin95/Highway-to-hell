package highwaytoken;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		ArrayList<ArrayList<String>> words = new ArrayList<ArrayList<String>>();
		ArrayList<String> highways = new ArrayList<String>();
		for(int i=0;i<52;i++) {
			words.add(new ArrayList<String>()); 
		}
		boolean dup = false;
		boolean fin = false;
		try {
			ArrayList<BufferedReader> reader = new ArrayList<BufferedReader>();

			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��ΰ�ӵ���.txt")));
			highways.add("��ΰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ΰ�ӵ���.txt")));
			highways.add("���ΰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��â����ӵ���.txt")));
			highways.add("��â����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ִ뱸��ӵ���.txt")));
			highways.add("���ִ뱸��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ֿ��ְ�ӵ���.txt")));
			highways.add("���ֿ��ְ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(��õ-�λ�).txt")));
			highways.add("���ذ�ӵ���(��õ-�λ�)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(����-��õ).txt")));
			highways.add("���ذ�ӵ���(����-��õ)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������1��ӵ�������.txt")));
			highways.add("������1��ӵ�������");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���õ�Ȱ�ӵ���.txt")));
			highways.add("���õ�Ȱ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(����-����).txt")));
			highways.add("����������ӵ���(����-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(����-����).txt")));
			highways.add("����������ӵ���(����-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(û��-����).txt")));
			highways.add("����������ӵ���(û��-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������μ�ȯ��ӵ���.txt")));
			highways.add("�������μ�ȯ��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(�λ�-���).txt")));
			highways.add("���ذ�ӵ���(�λ�-���)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(��ô-����).txt")));
			highways.add("���ذ�ӵ���(��ô-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(���-����).txt")));
			highways.add("���ذ�ӵ���(���-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ȱ��ְ�ӵ���.txt")));
			highways.add("���ȱ��ְ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�λ�ܰ���ȯ��ӵ���.txt")));
			highways.add("�λ�ܰ���ȯ��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ֿ�õ��ӵ���.txt")));
			highways.add("���ֿ�õ��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ӵ���.txt")));
			highways.add("�������ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����ܰ���ȯ��ӵ���.txt")));
			highways.add("����ܰ���ȯ��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ���ְ�ӵ���.txt")));
			highways.add("��õ���ְ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ؾȰ�ӵ���.txt")));
			highways.add("���ؾȰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���(����-��õ).txt")));
			highways.add("������õ��ӵ���(����-��õ)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���(����-����).txt")));
			highways.add("������õ��ӵ���(����-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��������2��ȯ��ӵ���(����-��ź).txt")));
			highways.add("��������2��ȯ��ӵ���(����-��ź)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��������2��ȯ��ӵ���(��õ-����).txt")));
			highways.add("��������2��ȯ��ӵ���(��õ-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ���ְ�ӵ���.txt")));
			highways.add("��õ���ְ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ƻ�û�ְ�ӵ���(����-��â).txt")));
			highways.add("�ƻ�û�ְ�ӵ���(����-��â)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������ӵ���.txt")));
			highways.add("������ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���μ����ӵ���.txt")));
			highways.add("���μ����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����ӵ���.txt")));
			highways.add("����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ͻ����װ�ӵ���(�뱸-����).txt")));
			highways.add("�ͻ����װ�ӵ���(�뱸-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ͻ����װ�ӵ���(�ͻ�-���).txt")));
			highways.add("�ͻ����װ�ӵ���(�ͻ�-���)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ�������װ�ӵ���.txt")));
			highways.add("��õ�������װ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(�۵�-����).txt")));
			highways.add("��2���ΰ�ӵ���(�۵�-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(�Ⱦ�-����).txt")));
			highways.add("��2���ΰ�ӵ���(�Ⱦ�-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(��õ�뱳).txt")));
			highways.add("��2���ΰ�ӵ���(��õ�뱳)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���.txt")));
			highways.add("��2���ΰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2�ߺΰ�ӵ���.txt")));
			highways.add("��2�ߺΰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ߺΰ�ӵ���.txt")));
			highways.add("�ߺΰ�ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ߺγ�����ӵ���.txt")));
			highways.add("�ߺγ�����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(�λ�-�뱸).txt")));
			highways.add("�߾Ӱ�ӵ���(�λ�-�뱸)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(���-�뵿).txt")));
			highways.add("�߾Ӱ�ӵ���(���-�뵿)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(��õ-��ȣ).txt")));
			highways.add("�߾Ӱ�ӵ���(��õ-��ȣ)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�뿵������ӵ���.txt")));
			highways.add("�뿵������ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ý����ӵ���.txt")));
			highways.add("���ý����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���.txt")));
			highways.add("������õ��ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ְ�ӵ���(����-����).txt")));
			highways.add("�������ְ�ӵ���(����-����)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ְ�ӵ���(����-ȭ��).txt")));
			highways.add("�������ְ�ӵ���(����-ȭ��)");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\ȣ����ӵ���.txt")));
			highways.add("ȣ����ӵ���");
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\ȣ����ӵ�������.txt")));
			highways.add("ȣ����ӵ�������");
			

			for (int k = 0; k < reader.size(); k++) {
				String line = null;
				line = reader.get(k).readLine();
				words.get(k).add(line);// 1����
				line = reader.get(k).readLine();
				words.get(k).add(line);// 2����
				String init = line;// 1����
				while ((line = reader.get(k).readLine()) != null) {

					
					if(fin) {
						fin = false;
						break;
					}
					StringTokenizer st = new StringTokenizer(line, "<|>|\"");

					
					
					while (st.hasMoreTokens()) {
						String buf = st.nextToken();
						if(buf.contains("roadsHavingContent")) {
							fin = true;
							break;
						}
						if (buf.contains(init + "~")) {
							StringTokenizer st1 = new StringTokenizer(buf, "~");
							st1.nextToken();
							buf = st1.nextToken();
							for (int i = 0; i < words.size(); i++)
								if (buf.equals(words.get(i))) {
									dup = true;
									break;
								}
							if (!dup) {
								words.get(k).add(buf);
								init = buf;
							}
							dup = false;
						}
						

					}

				}
			}
			for (int i = 0; i < reader.size(); i++) {
				reader.get(i).close();
			}

		} catch (FileNotFoundException e) {
			System.out.println("filenot");
		} catch (IOException e) {
			System.out.println(e);
		}

		for (int k = 0; k < words.size(); k++) {
			String insert = "insert into highways(id,name,num";
			String values = "values('way"+(k+1)+"','"+ highways.get(k)+"',"+words.get(k).size();
			String resultofinsertion = "";
			//System.out.println("CREATE TABLE way"+(k+1)+" (");
			///System.out.println("  date date NOT NULL,");
			//System.out.println("  time time NOT NULL,");
			for (int i = 0; i < words.get(k).size()-1; i++) {// ��������� �˾Ƽ�
				//System.out.println("  h"+(i+1)+"_h"+(i+2)+" int(11) DEFAULT NULL,");
				insert += ",h"+(i+1);
				values += ",'"+words.get(k).get(i)+"'";//insert into highways(name, num, h1 , ,,  ,h129) values('��ӵ���','',,,,,,,null);
				//System.out.print(words.get(k).get(i)+" ");
				
			}
			for (int i = words.get(k).size(); i > 1; i--) {// ��������� �˾Ƽ�
				//System.out.println("  h"+i+"_h"+(i-1)+" int(11) DEFAULT NULL,");
				//System.out.print(words.get(k).get(i)+" ");
				
			}
			//System.out.println("  PRIMARY KEY (date, time)");
			//System.out.println(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;");
			  

			resultofinsertion += insert + ") " +values + ");";
			System.out.println(resultofinsertion);
			//System.out.println("\n"+words.get(k).size());
		}
		//for(int i=1;i<=52;i++) {
		//	System.out.println("update highways");
		//	System.out.println("set ID = 'way"+i+"'");
		//	System.out.println("where name = '"+highways.get(i-1)+"';"); 
		//}

	}

}
