package TestUnit;

import TestUtil.conText;

public class totalTest{
	//Tag for Log
	private static final String Tag = "## totalTest :";
	private int times = conText.thread_run; //执行次数
	private String devices = null; //手机识别号
	
	public totalTest(String s){
		this.devices = s;
		Start();
	}
	
	public void Start() {
		System.out.println(Tag+ "start()" +" ##");
		new getCpuTest(devices, times).start();	//进行Cpu数据采集
		new getBatteryTest(devices, times).start();	//进行电量数据采集
		new getMemTest(devices, times).start();	//进行内存数据采集
	}
	
}
