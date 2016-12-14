package TestUnit;

import java.text.SimpleDateFormat;
import java.util.Date;

import TestUtil.FileUtil;
import TestUtil.PhoneUtil;
import TestUtil.conText;

public class getMemTest extends Thread{
	//Tag for Log
	private static final String Tag = "## getMemTest :";
	
	private String devices = null;
	private int times = 10;
	private int loop = 0;
	private String result = null;
	private String mem_cmd = null;
	public getMemTest(String s, int times) {
		this.devices = s;
		this.times = times;
		mem_cmd = conText.adb_s + devices + conText.mem_info + conText.pkgName_zm;
	}
	
	StringBuilder sb = new StringBuilder();
	
	@Override
	public void run() {
		sb.append("ÄÚ´æ²âÊÔ£º").append("\r\n");
		sb.append("Native Heap").append("|").append("Dalvik Heap")
			.append("|").append("TOTAL").append("|").append("time").append("\r\n");
		while (loop < times) {
			result = PhoneUtil.get_mem_info(mem_cmd);
			sb.append(result).append("\t").append((new SimpleDateFormat("yyyyMMddHHmmss")).format(new Date())).append("\r\n");
			loop += 1;
			try {
				Thread.sleep(3500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		//System.out.println(sb.toString());
		System.out.println(Tag+" Memory_test over" + " ##");
		FileUtil.save2local(sb.toString(),"MemTest_"+devices+"_"+(new SimpleDateFormat("yyyyMMddHHmmss")).format(new Date())+".txt");
	}
}
