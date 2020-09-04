//
//  AddCourseViewController.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol AddCourseViewControllerDelegate <NSObject>

@optional
- (void)addCourseViewControllerSaveWithFlag:(BOOL)flag;

@end

@interface AddCourseViewController : UIViewController

@property (nonatomic,weak) IBOutlet UITextField *txtName;
@property (nonatomic,weak) id<AddCourseViewControllerDelegate> delegate;
@property (nonatomic,strong) Course* inputCourse;

@end
