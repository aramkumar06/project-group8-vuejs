package com.ssafy.model.dto;

import java.sql.Date;

public class Trend {
	private int tno;
	private int yno;
	private Date recordDate;
	private int pointSubscriber;
	private int difSubscriber;
	private int pointView;
	private int difView;

	public int getTno() {
		return tno;
	}
	public void setTno(int tno) {
		this.tno = tno;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
	public Date getRecordDate() {
		return recordDate;
	}
	public void setRecordDate(Date recordDate) {
		this.recordDate = recordDate;
	}
	public int getPointSubscriber() {
		return pointSubscriber;
	}
	public void setPointSubscriber(int pointSubscriber) {
		this.pointSubscriber = pointSubscriber;
	}
	public int getDifSubscriber() {
		return difSubscriber;
	}
	public void setDifSubscriber(int difSubscriber) {
		this.difSubscriber = difSubscriber;
	}
	public int getPointView() {
		return pointView;
	}
	public void setPointView(int pointView) {
		this.pointView = pointView;
	}
	public int getDifView() {
		return difView;
	}
	public void setDifView(int difView) {
		this.difView = difView;
	}
}