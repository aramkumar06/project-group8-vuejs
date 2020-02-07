package com.ssafy.model.dto;

import java.sql.Date;

public class Community {
	private int cono;
	private int yno;
	private String articleTitle;
	private String articleLink;
	private String articleDescription;
	private Date articleDate;
	
	public int getCono() {
		return cono;
	}
	public void setCono(int cono) {
		this.cono = cono;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
	public String getArticleTitle() {
		return articleTitle;
	}
	public void setArticleTitle(String articleTitle) {
		this.articleTitle = articleTitle;
	}
	public String getArticleLink() {
		return articleLink;
	}
	public void setArticleLink(String articleLink) {
		this.articleLink = articleLink;
	}
	public String getArticleDescription() {
		return articleDescription;
	}
	public void setArticleDescription(String articleDescription) {
		this.articleDescription = articleDescription;
	}
	public Date getArticleDate() {
		return articleDate;
	}
	public void setArticleDate(Date articleDate) {
		this.articleDate = articleDate;
	}
}