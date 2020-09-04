//
//  CourseListViewController.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "CourseListViewController.h"

@interface CourseListViewController ()

@end

@implementation CourseListViewController

@synthesize tblData;

- (void)viewDidLoad {
    [super viewDidLoad];
    [self setUpView];
}

#pragma mark - Methods

- (void)setUpView {
    [self setTitle:@"Course List"];
    
    UIButton *btn = [[UIButton alloc]initWithFrame:CGRectMake(0, 0, 35, 35)];
    [btn setTitle:@"+" forState:UIControlStateNormal];
    [btn setTitleColor:[UIColor blackColor] forState:UIControlStateNormal];
    btn.titleLabel.font = [UIFont systemFontOfSize:30];
    [btn addTarget:self action:@selector(addCourseAction) forControlEvents:UIControlEventTouchUpInside];
    
    UIBarButtonItem *item = [[UIBarButtonItem alloc]initWithCustomView:btn];
    [self.navigationItem setRightBarButtonItem:item];
    
    [tblData setFrame:CGRectMake(0, STATUS_HEIGHT+NAVIGATION_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT-STATUS_HEIGHT-NAVIGATION_HEIGHT)];
    [tblData registerNib:[UINib nibWithNibName:@"CourseTableViewCell" bundle:nil] forCellReuseIdentifier:@"Cell"];
    tblData.dataSource = self;
    tblData.delegate = self;
    
    [self getData];
}

- (void)addCourseAction {
    AddCourseViewController *addView = [[AddCourseViewController alloc]init];
    addView.delegate = self;
    [self presentViewController:addView animated:true completion:nil];
}

- (void)getData {
    courseList = [[NSMutableArray alloc]init];
    [courseList addObjectsFromArray:[[ContentManager sharedManager] getAllCourses]];
    [tblData reloadData];
}

#pragma mark - AddCourseViewController's delegate

- (void)addCourseViewControllerSaveWithFlag:(BOOL)flag {
    if (flag) {
        [self getData];
    }
}

#pragma mark - UITableView's delegate

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return [courseList count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    CourseTableViewCell *cell = [tblData dequeueReusableCellWithIdentifier:@"Cell"];
    [cell setCellWithCourse:[courseList objectAtIndex:[indexPath row]] atIndex:indexPath];
    cell.delegate = self;
    return cell;
}

- (void)courseTableViewCellDeleteAtIndex:(NSIndexPath *)index {
    if([[ContentManager sharedManager] deleteCourse:[courseList objectAtIndex:[index row]]]) {
        [courseList removeObjectAtIndex:[index row]];
        [tblData beginUpdates];
        [tblData deleteRowsAtIndexPaths:@[index] withRowAnimation:UITableViewRowAnimationLeft];
        [tblData endUpdates];
        [tblData reloadData];
    }
}

- (void)courseTableViewCellEditAtIndex:(NSIndexPath *)index {
    AddCourseViewController *addView = [[AddCourseViewController alloc]init];
    addView.inputCourse = [courseList objectAtIndex:index.row];
    addView.delegate = self;
    [self presentViewController:addView animated:true completion:nil];
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(nonnull NSIndexPath *)indexPath {
    StudentListViewController* studentView = [[StudentListViewController alloc] init];
    studentView.inputCourse = [courseList objectAtIndex:indexPath.row];
    [self.navigationController pushViewController:studentView animated:YES];
}

@end
