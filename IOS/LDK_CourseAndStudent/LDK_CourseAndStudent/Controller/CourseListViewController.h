//
//  CourseListViewController.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CourseListViewController : UIViewController<UITableViewDataSource,UITableViewDelegate, AddCourseViewControllerDelegate, CourseTableViewCellDelegate>
{
    NSMutableArray *courseList;
}

@property (nonatomic,weak) IBOutlet UITableView *tblData;

@end

