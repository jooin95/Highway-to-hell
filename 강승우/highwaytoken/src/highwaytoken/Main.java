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
			
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\경부고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\경인고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\고창담양고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\광주대구고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\광주원주고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\남해고속도로(순천-부산).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\남해고속도로(영암-순천).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\남해제1고속도로지선.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\논산천안고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\당진영덕고속도로(대전-당진).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\당진영덕고속도로(상주-영덕).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\당진영덕고속도로(청주-상주).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\대전남부순환고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\동해고속도로(부산-울산).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\동해고속도로(삼척-속초).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\동해고속도로(울산-포항).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\무안광주고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\부산외곽순환고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\상주영천고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\서울양양고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\서울외곽순환고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\서천공주고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\서해안고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\세종포천고속도로(구리-포천).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\세종포천고속도로(양주-소흘).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\수도권제2순환고속도로(봉담-동탄).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\수도권제2순환고속도로(인천-김포).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\순천완주고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\아산청주고속도로(옥산-오창).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\영동고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\용인서울고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\울산고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\익산포항고속도로(대구-포항).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\익산포항고속도로(익산-장수).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\인천국제공항고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\제2경인고속도로(송도-연수).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\제2경인고속도로(안양-성남).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\제2경인고속도로(인천대교).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\제2경인고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\제2중부고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\중부고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\중부내륙고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\중앙고속도로(부산-대구).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\중앙고속도로(삼락-대동).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\중앙고속도로(춘천-금호).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\통영대전고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\평택시흥고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\평택제천고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\평택파주고속도로(수원-광명).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\평택파주고속도로(평택-화성).txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\호남고속도로.txt")));
			reader.add(new BufferedReader(new FileReader("C:\\Users\\woo\\Desktop\\high\\호남고속도로지선.txt")));
			

			for (int k = 0; k < reader.size(); k++) {
				String line = null;
				line = reader.get(k).readLine();
				words.get(k).add(line);// 1구간
				line = reader.get(k).readLine();
				words.get(k).add(line);// 2구간
				String init = line;// 1구간
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
			for (int i = 0; i < words.get(k).size(); i++) {// 출력형식은 알아서
				System.out.print(words.get(k).get(i)+" ");
			}
			System.out.println("\n"+words.get(k).size());
		}

	}

}
