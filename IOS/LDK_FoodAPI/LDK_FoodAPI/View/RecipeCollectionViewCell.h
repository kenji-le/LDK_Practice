//
//  RecipeCollectionViewCell.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface RecipeCollectionViewCell : UICollectionViewCell

@property (weak, nonatomic) IBOutlet UIImageView *imgRecipe;
@property (weak, nonatomic) IBOutlet UILabel *lblTitle;
@property (weak, nonatomic) Recipe *currentRecipe;

- (void)setCellWithRecipe:(Recipe *)recipe;

@end
