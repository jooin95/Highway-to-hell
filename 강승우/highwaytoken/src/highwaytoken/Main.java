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
		for(int i=0;i<52;i++) {
			words.add(new ArrayList<String>()); 
		}
		boolean dup = false;
		boolean fin = false;
		try {
			ArrayList<BufferedReader> reader = new ArrayList<BufferedReader>();
			
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��ΰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ΰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��â����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ִ뱸��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ֿ��ְ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(��õ-�λ�).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(����-��õ).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������1��ӵ�������.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���õ�Ȱ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(����-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(����-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����������ӵ���(û��-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������μ�ȯ��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(�λ�-���).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(��ô-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ذ�ӵ���(���-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ȱ��ְ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�λ�ܰ���ȯ��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ֿ�õ��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����ܰ���ȯ��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ���ְ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ؾȰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���(����-��õ).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���(����-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��������2��ȯ��ӵ���(����-��ź).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��������2��ȯ��ӵ���(��õ-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ���ְ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ƻ�û�ְ�ӵ���(����-��â).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���μ����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ͻ����װ�ӵ���(�뱸-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ͻ����װ�ӵ���(�ͻ�-���).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��õ�������װ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(�۵�-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(�Ⱦ�-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���(��õ�뱳).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2���ΰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\��2�ߺΰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ߺΰ�ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�ߺγ�����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(�λ�-�뱸).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(���-�뵿).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�߾Ӱ�ӵ���(��õ-��ȣ).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�뿵������ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\���ý����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\������õ��ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ְ�ӵ���(����-����).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\�������ְ�ӵ���(����-ȭ��).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\ȣ����ӵ���.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\ȣ����ӵ�������.txt")));
			

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
			for (int i = 0; i < words.get(k).size(); i++) {// ��������� �˾Ƽ�
				System.out.print(words.get(k).get(i)+" ");
			}
			System.out.println("\n"+words.get(k).size());
		}

	}

}
