import { Component, OnInit } from '@angular/core';
import { GetwineService } from '../getwine.service';


@Component({
  selector: 'app-winelist',
  templateUrl: './winelist.component.html',
  styleUrls: ['./winelist.component.css']
})
export class WinelistComponent implements OnInit {

  public wineList;
  public curr_page = 1;
  public country = '';
  public province = '';
  public region_1 = '';
  public region_2 = '';
  public page = this.curr_page;
  public total_pages;
  public sort_order = 'ASC';
  constructor(private getwineService: GetwineService ) {

  }

  ngOnInit() {
    this.getPage('curr');
  }

  public getPage(to){
    const that = this;
    var params = {
      'format': 'json',
    };

    if(to=='next'){
      this.page=Math.min(this.curr_page+1, this.total_pages);
      this.curr_page = this.page;
    }
    else if(to=='prev'){
      this.page=Math.max(1, this.curr_page-1);
      this.curr_page = this.page;
    }

    if(to == 'sort'){
      this.sort_order = this.sort_order == 'ASC' ? 'DESC' : 'ASC';
      params['sort_order'] = this.sort_order;
    }

    console.log(this.page);
    params['page'] = this.page;
    if(this.country != '') params['country'] = this.country;
    if(this.province != '') params['province'] = this.province;
    if(this.region_1 != '') params['region_1'] = this.region_1;
    if(this.region_2 != '') params['region_2'] = this.region_2;

    console.log(params);

    this.getwineService.getWineList(params).subscribe(function(wines){
      that.wineList = wines.results;
      that.total_pages = Math.ceil(wines.count/10);
      console.log(that.wineList);
    });
  }

}
