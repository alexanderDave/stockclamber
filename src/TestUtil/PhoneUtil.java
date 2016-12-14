package TestUtil;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class PhoneUtil {
	// Tag for Log
	public static final String Tag = "##PhoneUtil : ";
	
	/**
	 * 执行cmd命令并返回执行结果
	 * @param cmd 可直接从conText类的文本库中获取，方便后期内容修改
	 * @return Sting 返回文本 （文本的解析在实际中重复，后期根据实际需求优化返回类型）
	 * @author daiw 20161208
	 */
	public static String excuteCmd(String cmd, String temp) {
		System.out.println(Tag+"excuteCmd- "+ cmd+" ##");
		BufferedReader br = null;
		br = new BufferedReader(new InputStreamReader(excuteCmd4ips(cmd)));
		StringBuilder sb = new StringBuilder();
		String line = null;
		if ("" == temp) {
			try {
				while ((line = br.readLine())!= null) {
					if (!line.equals("")) {
						sb.append(line);
						sb.append("\r\n");
					}				
				}
			} catch (IOException e) {
				e.printStackTrace();
			} finally{
				
				try {
					if(br!=null)
						br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		} else {
			try {
				while ((line = br.readLine())!= null) {
					if (!line.equals("")) {
						if (line.contains(temp)) {
							sb.append(line);
							sb.append("\r\n");
						}
					}				
				}
			} catch (IOException e) {
				e.printStackTrace();
			} finally{
				
				try {
					if(br!=null)
						br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return sb.toString();
	}
	
	/**
	 * 执行cmd命令获取与之对应返回输出值的inputstream
	 * @param cmd cmd命令
	 * @return inputstream 输出字符流
	 */
	public static InputStream excuteCmd4ips(String cmd) {
		InputStream in = null;
		try {
			Process p = Runtime.getRuntime().exec(cmd);
			in = p.getInputStream();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return in;
	}
	
	/**
	 * 直接运行cmd命令
	 * @param cmd
	 */
	public static void runCmd(String cmd){
		try {
			Runtime.getRuntime().exec(cmd);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	 * 获取当前链接的所有手机的模拟器编号
	 * @return List<String> 
	 * @author daiw 20161208 
	 */
	public static List<String> getPhoneserNum(){
		System.out.println(Tag+"getPhoneserNum "+" ##");
		List<String> phone_Ser_num = null;
		String adbdevices = PhoneUtil.excuteCmd(conText.show_devices,"");
		if (!adbdevices.equals("false")) {
			phone_Ser_num = new ArrayList<String>();
			String temp = null;
			BufferedReader br = new BufferedReader(new InputStreamReader(
							new ByteArrayInputStream(adbdevices.getBytes())));
			String line = null;
			try {
				while ((line = br.readLine())!= null) {
					temp = line;
					if (temp.contains("device") && !temp.contains("att") && !temp.contains("deamon")) {
						String serNum = temp.substring(0, temp.lastIndexOf("d")).trim();
						System.out.println(serNum);
						phone_Ser_num.add(serNum);
					}
				}
			} catch (IOException e) {
				return null;
			}
		}	
		return phone_Ser_num;
	}
	
	/**
	 * 获取apk在当前手机运行的进程id
	 * @param in 执行对应的cmd命令获得的返回值信息
	 * @return pid 返回当前进行的字符串 便于后期操作
	 * @author daiw 20161212
	 */
	public static String get_pkg_pid(String in){
		System.out.println(Tag+"get_pkg_pid "+" ##");
		String pid = in.replaceAll(" ", ",").replaceAll(",+", ":").split(":")[1];
		return pid;
	}

	/**
	 * 获取被测试应用在执行过程中占用cpu的百分比
	 * @param cmd String cmd命令
	 * @return result String 版本比
	 * @author daiw 20161212
	 */
	public static String get_cpu_percent(String cmd){
		System.out.println(Tag+"get_cpu_percent "+" ##");
		String percent = excuteCmd(cmd,"TOTAL");
		String result = null;
		if (percent != "") {
			try {
				result = percent.split(" ")[0];
			} catch (Exception e) {
				result = "-";
			}			
		}else {
			result = "-";
		}		
		return result;
	}

	public static String get_mem_info(String cmd){
		System.out.println(Tag+"get_mem_info "+" ##");
		
		String natives = null, dalviks = null, totals = null;
		String result = null;
		StringBuilder sb = new StringBuilder();
//		System.out.println(excuteCmd(cmd, "Native Heap").replaceAll(" +", ","));
//		System.out.println(excuteCmd(cmd, "Native Heap").replaceAll(" +", ",").split(",")[3]);
//		System.out.println(excuteCmd(cmd, "Dalvik Heap").replaceAll(" +", ","));
//		System.out.println(excuteCmd(cmd, "Dalvik Heap").replaceAll(" +", ",").split(",")[3]);
//		System.out.println(excuteCmd(cmd, "TOTAL").replaceAll(" +", ","));
//		System.out.println(excuteCmd(cmd, "TOTAL").replaceAll(" +", ",").split(",")[2]);
		
		natives = excuteCmd(cmd, "Native Heap").replaceAll(" +", ",").split(",")[3];
		dalviks = excuteCmd(cmd, "Dalvik Heap").replaceAll(" +", ",").split(",")[3];
		totals = excuteCmd(cmd, "TOTAL").replaceAll(" +", ",").split(",")[2];
		
		float a  = (float)Integer.parseInt(natives)/1024;
		float b  = (float)Integer.parseInt(dalviks)/1024;
		float c  = (float)Integer.parseInt(totals)/1024;
		result = sb.append(a).append("M\t").append(b).append("M\t").append(c).append("M").toString();
		return result;
	}

	public static boolean judge(String devices) {
		String version = excuteCmd(conText.adb_s+devices+conText.get_sys_version,"");
		int first = version.charAt(0);
		int sec = version.charAt(2);
		
		if (first > 4 || (first <=4 && sec <= 4)) 
			return true;
		else 
			return false;
	}
}
