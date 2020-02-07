package com.ssafy.model.dto;

import java.sql.Date;

public class User {
	private int usno;
	private String userID;
	private String userEmail;
	private String userName;
	private Date regDate;
	
	public String getUserID() {
		return userID;
	}
	public void setUserID(String userID) {
		this.userID = userID;
	}
	public int getUsno() {
		return usno;
	}
	public void setUsno(int usno) {
		this.usno = usno;
	}
	public String getUserEmail() {
		return userEmail;
	}
	public void setUserEmail(String userEmail) {
		this.userEmail = userEmail;
	}
	public String getUserName() {
		return userName;
	}
	public void setUserName(String userName) {
		this.userName = userName;
	}
	public Date getRegDate() {
		return regDate;
	}
	public void setRegDate(Date regDate) {
		this.regDate = regDate;
	}
}