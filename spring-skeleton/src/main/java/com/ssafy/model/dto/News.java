package com.ssafy.model.dto;

import java.sql.Date;

public class News {
	private int nno;
	private int yno;
	private String newsLink;
	private String newsTitle;
	private String newsDescription;
	private Date newsDate;
	private String pressName;
	private int clickCount;
	
	public int getNno() {
		return nno;
	}
	public void setNno(int nno) {
		this.nno = nno;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
	public String getNewsLink() {
		return newsLink;
	}
	public void setNewsLink(String newsLink) {
		this.newsLink = newsLink;
	}
	public String getNewsTitle() {
		return newsTitle;
	}
	public void setNewsTitle(String newsTitle) {
		this.newsTitle = newsTitle;
	}
	public String getNewsDescription() {
		return newsDescription;
	}
	public void setNewsDescription(String newsDescription) {
		this.newsDescription = newsDescription;
	}
	public Date getNewsDate() {
		return newsDate;
	}
	public void setNewsDate(Date newsDate) {
		this.newsDate = newsDate;
	}
	public String getPressName() {
		return pressName;
	}
	public void setPressName(String pressName) {
		this.pressName = pressName;
	}
	public int getClickCount() {
		return clickCount;
	}
	public void setClickCount(int clickCount) {
		this.clickCount = clickCount;
	}
}