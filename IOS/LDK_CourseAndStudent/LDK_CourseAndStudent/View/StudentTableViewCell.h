//
//  StudentTableViewCell.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol StudentTableViewCellDelegate <NSObject>

@optional
- (void)studentTableViewCellDeleteAtIndex:(NSIndexPath *)index;
- (void)studentTableViewCellEditAtIndex:(NSIndexPath *)index;

@end

@interface StudentTableViewCell : UITableViewCell
{
    NSIndexPath *currentIndex;
}

@property (nonatomic,weak) IBOutlet UILabel *lblName;
@property (nonatomic,weak) id<StudentTableViewCellDelegate> delegate;

- (void)setCellWithStudent:(Student *)student atIndex:(NSIndexPath *)index;

@end
