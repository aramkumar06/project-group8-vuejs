package com.ssafy.model.dto;

import java.sql.Date;

public class Favorite {
	private int usno;
	private int yno;
	private Date regDate;
	
	public int getUsno() {
		return usno;
	}
	public void setUsno(int usno) {
		this.usno = usno;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
	public Date getRegDate() {
		return regDate;
	}
	public void setRegDate(Date regDate) {
		this.regDate = regDate;
	}
}