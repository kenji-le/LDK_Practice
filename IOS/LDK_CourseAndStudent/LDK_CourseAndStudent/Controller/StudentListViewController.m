//
//  StudentListViewController.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "StudentListViewController.h"

@interface StudentListViewController ()

@end

@implementation StudentListViewController

@synthesize tblStudents;
@synthesize inputStudent;
@synthesize inputCourse;

- (void)viewDidLoad {
    [super viewDidLoad];
    [self setUpView];
}

#pragma mark - Methods

- (void)setUpView {
    [self setTitle:@"Student List"];
    
    UIButton *btn = [[UIButton alloc]initWithFrame:CGRectMake(0, 0, 35, 35)];
    [btn setTitle:@"+" forState:UIControlStateNormal];
    [btn setTitleColor:[UIColor blackColor] forState:UIControlStateNormal];
    btn.titleLabel.font = [UIFont systemFontOfSize:30];
    [btn addTarget:self action:@selector(addStudentAction) forControlEvents:UIControlEventTouchUpInside];
    
    UIBarButtonItem *item = [[UIBarButtonItem alloc]initWithCustomView:btn];
    [self.navigationItem setRightBarButtonItem:item];
    
    [tblStudents setFrame:CGRectMake(0, STATUS_HEIGHT+NAVIGATION_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT-STATUS_HEIGHT-NAVIGATION_HEIGHT)];
    [tblStudents registerNib:[UINib nibWithNibName:@"StudentTableViewCell" bundle:nil] forCellReuseIdentifier:@"Cell"];
    tblStudents.dataSource = self;
    tblStudents.delegate = self;
    
    [self getData];
    
}

- (void)getData {
    studentList = [[NSMutableArray alloc] init];
    [studentList addObjectsFromArray:[[inputCourse hasStudents] allObjects]];
    
    NSSortDescriptor *sort = [NSSortDescriptor sortDescriptorWithKey:@"studentName" ascending:YES comparator:^NSComparisonResult(id obj1, id obj2) {
        return [(NSString *)obj1 compare:(NSString *)obj2 options:NSNumericSearch];
    }];
    
    [studentList sortUsingDescriptors:[NSArray arrayWithObject:sort]];
    [tblStudents reloadData];
}

- (void)addStudentAction {
    AddStudentViewController *addView = [[AddStudentViewController alloc] init];
    addView.delegate = self;
    addView.inputCourse = inputCourse;
    [self presentViewController:addView animated:true completion:nil];
}

#pragma mark - AddStudentViewController's delegate

- (void)addStudentViewControllerSaveWithFlag:(BOOL)flag {
    if (flag) {
        [self getData];
    }
}

#pragma mark - UITableView's delegate

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return studentList.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    StudentTableViewCell *cell = [tblStudents dequeueReusableCellWithIdentifier:@"Cell"];
    [cell setCellWithStudent:[studentList objectAtIndex:indexPath.row] atIndex:indexPath];
    cell.delegate = self;
    return cell;
}

- (void)studentTableViewCellDeleteAtIndex:(NSIndexPath *)index {
    if ([[ContentManager sharedManager] deleteStudent:[studentList objectAtIndex:index.row]]) {
        [studentList removeObjectAtIndex:index.row];
        [tblStudents beginUpdates];
        [tblStudents deleteRowsAtIndexPaths:@[index] withRowAnimation:UITableViewRowAnimationLeft];
        [tblStudents endUpdates];
        [tblStudents reloadData];
    }
}

- (void)studentTableViewCellEditAtIndex:(NSIndexPath *)index {
    AddStudentViewController *addView = [[AddStudentViewController alloc] init];
    addView.inputStudent = [studentList objectAtIndex:index.row];
    addView.delegate = self;
    [self presentViewController:addView animated:true completion:nil];
}

- (void)tableView:(UITableView *)tableView didDeselectRowAtIndexPath:(NSIndexPath *)indexPath {
    StudentListViewController *studentView = [[StudentListViewController alloc] init];
    studentView.inputStudent = [studentList objectAtIndex:indexPath.row];
    [self.navigationController pushViewController:studentView animated:YES];
}

@end
