package TestUnit;

import java.text.SimpleDateFormat;
import java.util.Date;

import TestUtil.FileUtil;
import TestUtil.PhoneUtil;
import TestUtil.conText;

public class getCpuTest extends Thread{
	//Tag for Log
	private static final String Tag = "## getCpuTest :";
	private String devices = null;
	private int times = 10;
	private int loop = 0;
	private String percent = null;
	private String cpu_cmd = null;
	public getCpuTest(String s, int times) {
		this.devices = s;
		this.times = times;
		cpu_cmd = conText.adb_s + devices + conText.cpu_info + conText.pkgName_zm;
	}
	
	StringBuilder sb = new StringBuilder();
	
	@Override
	public void run() {
		sb.append("Cpu ≤‚ ‘£∫").append("\r\n");
		while (loop < times) {
			percent = PhoneUtil.get_cpu_percent(cpu_cmd);
			sb.append(percent).append("--").append((new SimpleDateFormat("yyyyMMdd_HH:mm:ss")).format(new Date()));
			sb.append("\r\n");
			loop += 1;
			try {
				Thread.sleep(3500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		//System.out.println(sb.toString());
		System.out.println(Tag + "Cpu_test over ##");
		FileUtil.save2local(sb.toString(),"CpuTest_"+devices+"_"+(new SimpleDateFormat("yyyyMMddHHmmss")).format(new Date())+".txt");
	}
	
	
		
}
