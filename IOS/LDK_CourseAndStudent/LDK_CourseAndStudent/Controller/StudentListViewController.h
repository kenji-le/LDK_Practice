//
//  StudentListViewController.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface StudentListViewController : UIViewController<UITableViewDataSource,UITableViewDelegate,AddStudentViewControllerDelegate,StudentTableViewCellDelegate>
{
    NSMutableArray *studentList;
}

@property (nonatomic,weak) IBOutlet UITableView *tblStudents;
@property (nonatomic, strong) Student *inputStudent;
@property (nonatomic, strong) Course *inputCourse;

@end
